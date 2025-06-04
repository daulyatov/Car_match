from django.contrib import admin
from .models import Brand, CarModel, CarDetails

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'country')
    list_filter = ('country',)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'body_type')
    list_filter = ('brand', 'year', 'body_type')
    search_fields = ('name', 'brand__name')
    raw_id_fields = ('brand',)

@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'engine_type', 'horsepower', 'transmission')
    list_filter = ('engine_type', 'transmission')
    search_fields = ('car_model__name', 'car_model__brand__name')
    raw_id_fields = ('car_model',)
