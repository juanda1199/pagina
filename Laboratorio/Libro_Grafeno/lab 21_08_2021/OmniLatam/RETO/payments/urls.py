from rest_framework import routers
from .views import PaymentViewSet, PaymentOrderViewSet

router = routers.SimpleRouter()
router.register('payment', PaymentViewSet, basename='payment')
router.register('paymentOrder', PaymentOrderViewSet, basename='paymentOrder')
urlpatterns = router.urls
