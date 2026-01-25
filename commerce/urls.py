from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import ProduitViewSet, ClientViewSet, VenteViewSet, DetteViewSet, DashboardView, ProduitStatsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('core.urls')),

    # Endpoints API REST
    path('api/', include('core.urls')),

    # Endpoint de dashboard
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
    

    # Endpoints JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/stats/produit/<int:pk>/', ProduitStatsView.as_view(), name='produit_stats'),
]
