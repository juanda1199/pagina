from .models import Payment, PaymentOrder
from rest_framework import viewsets
from .serializers import PaymentSerializer, PaymentOrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentOrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PaymentOrderSerializer
    queryset = PaymentOrder.objects.all()
