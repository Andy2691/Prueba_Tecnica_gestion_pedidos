from rest_framework.viewsets import ModelViewSet
from .models import ElementoMenu
from .serializers import ElementoMenuSerializer

class ElementoMenuViewSet(ModelViewSet):
    """
    Vista para gestionar elementos del menú.
    Incluye las operaciones CRUD completas.
    """
    queryset = ElementoMenu.objects.all()
    serializer_class = ElementoMenuSerializer
