from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Brand, CarModel, CarDetails
from .serializers import (
    BrandSerializer, CarModelSerializer, CarDetailsSerializer
)

# Create your views here.

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

    def get_queryset(self):
        queryset = CarModel.objects.all()
        brand_id = self.request.query_params.get('brand_id', None)
        if brand_id is not None:
            queryset = queryset.filter(brand_id=brand_id)
        return queryset

class CarDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarDetails.objects.all()
    serializer_class = CarDetailsSerializer

    def get_object(self):
        car_model_id = self.kwargs.get('pk')
        return get_object_or_404(CarDetails, car_model_id=car_model_id)
