from rest_framework.viewsets import ModelViewSet
from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer, DetallePedidoSerializer

class PedidoViewSet(ModelViewSet):
    """
    Vista para gestionar pedidos.
    Incluye las operaciones CRUD completas.
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(ModelViewSet):
    """
    Vista para gestionar detalles de los pedidos.
    Incluye las operaciones CRUD completas.
    """
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
