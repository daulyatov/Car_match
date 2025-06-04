from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Brand, CarModel, CarDetails
from .serializers import (
    BrandSerializer, CarModelSerializer, CarDetailsSerializer,
    CompareCarsSerializer, CompareCarsResponseSerializer
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

class CompareViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CompareCarsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        car_model_ids = serializer.validated_data['car_model_ids']
        cars = []
        comparison = {}

        # Get all car models and their details
        car_models = CarModel.objects.filter(id__in=car_model_ids).select_related('brand', 'details')
        
        if len(car_models) != len(car_model_ids):
            return Response(
                {"error": "One or more car models not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Prepare car details for comparison
        for car_model in car_models:
            if not hasattr(car_model, 'details'):
                return Response(
                    {"error": f"Details not found for {car_model}"},
                    status=status.HTTP_404_NOT_FOUND
                )

            car_data = {
                'id': car_model.id,
                'name': str(car_model),
                'brand': car_model.brand.name,
                'year': car_model.year,
                'body_type': car_model.body_type,
                'engine_type': car_model.details.engine_type,
                'engine_size': car_model.details.engine_size,
                'horsepower': car_model.details.horsepower,
                'torque': car_model.details.torque,
                'transmission': car_model.details.transmission,
                'acceleration': car_model.details.acceleration,
                'top_speed': car_model.details.top_speed,
                'fuel_consumption': car_model.details.fuel_consumption,
                'weight': car_model.details.weight,
                'dimensions': f"{car_model.details.length}x{car_model.details.width}x{car_model.details.height}"
            }
            cars.append(car_data)

        # Create comparison data
        comparison = {
            'engine_size': [car['engine_size'] for car in cars],
            'horsepower': [car['horsepower'] for car in cars],
            'torque': [car['torque'] for car in cars],
            'acceleration': [car['acceleration'] for car in cars],
            'top_speed': [car['top_speed'] for car in cars],
            'fuel_consumption': [car['fuel_consumption'] for car in cars],
            'weight': [car['weight'] for car in cars]
        }

        response_data = {
            'cars': cars,
            'comparison': comparison
        }

        response_serializer = CompareCarsResponseSerializer(data=response_data)
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.validated_data)
