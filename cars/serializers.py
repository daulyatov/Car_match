from rest_framework import serializers
from .models import Brand, CarModel, CarDetails

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'brand_name', 'name', 'year', 'body_type', 'image', 'created_at', 'updated_at']

class CarDetailsSerializer(serializers.ModelSerializer):
    car_model_name = serializers.CharField(source='car_model.__str__', read_only=True)

    class Meta:
        model = CarDetails
        fields = '__all__'

class CompareCarsSerializer(serializers.Serializer):
    car_model_ids = serializers.ListField(
        child=serializers.IntegerField(),
        min_length=2,
        max_length=5
    )

class CompareCarsResponseSerializer(serializers.Serializer):
    cars = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
    comparison = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField()
        )
    ) 