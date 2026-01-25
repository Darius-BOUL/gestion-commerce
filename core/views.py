from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Produit, Client, Vente, Dette
from .serializers import ProduitSerializer, ClientSerializer, VenteSerializer, DetteSerializer

from rest_framework.views import APIView
from django.utils.timezone import now
from django.db.models import Sum


# Page d’accueil simple
def home(request):
    return JsonResponse({"message": "Bienvenue dans l'API de gestion de commerce"})


class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

    # Action personnalisée : annuler une vente et remettre le stock
    @action(detail=True, methods=['post'])
    def annuler(self, request, pk=None):
        vente = self.get_object()
        produit = vente.produit
        produit.stock += vente.quantite  # on remet le stock
        produit.save()
        vente.delete()
        return Response({'status': 'vente annulée et stock remis'}, status=status.HTTP_200_OK)


class DetteViewSet(viewsets.ModelViewSet):
    queryset = Dette.objects.all()
    serializer_class = DetteSerializer

    # Action personnalisée : marquer une dette comme payée
    @action(detail=True, methods=['post'])
    def payer(self, request, pk=None):
        dette = self.get_object()
        if not dette.payee:
            dette.payee = True
            dette.save()
            return Response({'status': 'dette payée'}, status=status.HTTP_200_OK)
        return Response({'status': 'déjà payée'}, status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    def get(self, request):
        today = now().date()
        month = today.month

        # Ventes du jour
        ventes_jour = Vente.objects.filter(date__date=today).aggregate(total=Sum('total'))['total'] or 0

        # Ventes du mois
        ventes_mois = Vente.objects.filter(date__month=month).aggregate(total=Sum('total'))['total'] or 0

        # Dettes en cours
        dettes_en_cours = Dette.objects.filter(payee=False).aggregate(total=Sum('montant'))['total'] or 0

        # Top 5 produits les plus vendus
        top_produits = (
            Vente.objects.values('produit__nom')
            .annotate(total_vendu=Sum('quantite'))
            .order_by('-total_vendu')[:5]
        )

        return Response({
            "ventes_jour": ventes_jour,
            "ventes_mois": ventes_mois,
            "dettes_en_cours": dettes_en_cours,
            "top_produits": list(top_produits),
        })


class ProduitStatsView(APIView):
    def get(self, request, pk):
        try:
            produit = Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            return Response({"error": "Produit introuvable"}, status=404)

        # Ventes liées au produit
        ventes = Vente.objects.filter(produit=produit)

        quantite_vendue = ventes.aggregate(total=Sum('quantite'))['total'] or 0
        chiffre_genere = ventes.aggregate(total=Sum('total'))['total'] or 0

        # Clients ayant acheté ce produit
        clients_ids = ventes.values_list('client_id', flat=True).distinct()

        # Dettes de ces clients
        dettes_associees = Dette.objects.filter(client_id__in=clients_ids, payee=False).aggregate(total=Sum('montant'))['total'] or 0

        return Response({
            "produit": produit.nom,
            "quantite_vendue": quantite_vendue,
            "chiffre_genere": chiffre_genere,
            "dettes_associees": dettes_associees,
        })
