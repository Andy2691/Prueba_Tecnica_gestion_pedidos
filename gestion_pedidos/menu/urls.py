from rest_framework.routers import DefaultRouter
from .views import ElementoMenuViewSet

router = DefaultRouter()
router.register(r'', ElementoMenuViewSet, basename='elementomenu')

urlpatterns = router.urls
