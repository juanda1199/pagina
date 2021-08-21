from .models import Order, OrderDetail
from rest_framework import viewsets
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
