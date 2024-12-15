from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    """
    Vista para gestionar usuarios.
    Incluye las operaciones CRUD completas.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
