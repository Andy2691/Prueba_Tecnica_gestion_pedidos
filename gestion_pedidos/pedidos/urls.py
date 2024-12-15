from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, DetallePedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'detalles', DetallePedidoViewSet, basename='detallepedido')

urlpatterns = router.urls
