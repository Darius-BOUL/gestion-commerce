from django.urls import path, include
from rest_framework import routers
from .views import ProduitViewSet, ClientViewSet, VenteViewSet, DetteViewSet, home

router = routers.DefaultRouter()
router.register(r'produits', ProduitViewSet, basename='produit')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'ventes', VenteViewSet, basename='vente')
router.register(r'dettes', DetteViewSet, basename='dette')

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]
