from rest_framework import serializers
from .models import Produit, Client, Vente, Dette


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class VenteSerializer(serializers.ModelSerializer):
    # Champs supplémentaires pour afficher les noms
    produit_nom = serializers.CharField(source='produit.nom', read_only=True)
    client_nom = serializers.CharField(source='client.nom', read_only=True)

    class Meta:
        model = Vente
        fields = ['id', 'produit', 'produit_nom', 'client', 'client_nom', 'quantite', 'total', 'date']
        read_only_fields = ['total', 'date', 'produit_nom', 'client_nom']


class DetteSerializer(serializers.ModelSerializer):
    # Champ supplémentaire pour afficher le nom du client
    client_nom = serializers.CharField(source='client.nom', read_only=True)

    class Meta:
        model = Dette
        fields = ['id', 'client', 'client_nom', 'montant', 'date', 'payee']
        read_only_fields = ['date', 'payee', 'client_nom']
