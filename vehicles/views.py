from rest_framework import viewsets
from .models import Brand, Vehicle
from .serializers import BrandSerializer, VehicleSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
# Create your views here.
