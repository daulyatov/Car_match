from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    logo = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    body_type = models.CharField(max_length=50)  # sedan, SUV, hatchback, etc.
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.year})"

    class Meta:
        ordering = ['brand', 'name', 'year']
        unique_together = ['brand', 'name', 'year']

class CarDetails(models.Model):
    car_model = models.OneToOneField(CarModel, on_delete=models.CASCADE, related_name='details')
    engine_type = models.CharField(max_length=50)  # petrol, diesel, electric, hybrid
    engine_size = models.FloatField()  # in liters
    horsepower = models.IntegerField()
    torque = models.IntegerField()  # in Nm
    transmission = models.CharField(max_length=50)  # automatic, manual
    acceleration = models.FloatField()  # 0-100 km/h in seconds
    top_speed = models.IntegerField()  # in km/h
    fuel_consumption = models.FloatField()  # in L/100km
    weight = models.IntegerField()  # in kg
    length = models.IntegerField()  # in mm
    width = models.IntegerField()  # in mm
    height = models.IntegerField()  # in mm
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Details for {self.car_model}"
