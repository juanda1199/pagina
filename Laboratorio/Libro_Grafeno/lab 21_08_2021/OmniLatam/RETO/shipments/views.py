from .models import City, Shipment
from rest_framework import viewsets
from .serializers import CitySerializer, ShipmentSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing notification instances.
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
