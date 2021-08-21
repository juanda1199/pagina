from rest_framework import routers
from .views import OrderViewSet, OrderDetailViewSet

router = routers.SimpleRouter()
router.register('order', OrderViewSet, basename='order')
router.register('orderDetail', OrderDetailViewSet, basename='orderDetail')
urlpatterns = router.urls
