from rest_framework.viewsets import ModelViewSet
from .models import Restaurante
from .serializers import RestauranteSerializer

class RestauranteViewSet(ModelViewSet):
    """
    Vista para gestionar restaurantes.
    Incluye las operaciones CRUD completas.
    """
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
