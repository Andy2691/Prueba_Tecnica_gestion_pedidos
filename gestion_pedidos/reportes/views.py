from rest_framework.viewsets import ModelViewSet
from .models import Reporte
from .serializers import ReporteSerializer

class ReporteViewSet(ModelViewSet):
    """
    Vista para gestionar reportes.
    Incluye las operaciones CRUD completas.
    """
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
