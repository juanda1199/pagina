from rest_framework import routers
from .views import CityViewSet, ShipmentViewSet

router = routers.SimpleRouter()
router.register('city', CityViewSet, basename='city')
router.register('shipment', ShipmentViewSet, basename='shipment')
urlpatterns = router.urls

