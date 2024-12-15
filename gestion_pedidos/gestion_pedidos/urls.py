from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rutas del administrador
    path('usuarios/', include('usuarios.urls')),  # Rutas de usuarios
    path('restaurantes/', include('restaurantes.urls')),  # Rutas de restaurantes
    path('menu/', include('menu.urls')),  # Rutas de menú
    path('pedidos/', include('pedidos.urls')),  # Rutas de pedidos
    path('reportes/', include('reportes.urls')),  # Rutas de reportes

    # Rutas de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
