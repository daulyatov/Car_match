from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Brand, CarModel, CarDetails

class CarModelTests(APITestCase):
    def setUp(self):
        # Create test brand
        self.brand = Brand.objects.create(
            name="Test Brand",
            country="Test Country",
            founded_year=2000
        )
        
        # Create test car model
        self.car_model = CarModel.objects.create(
            brand=self.brand,
            name="Test Model",
            year=2023,
            body_type="sedan"
        )
        
        # Create test car details
        self.car_details = CarDetails.objects.create(
            car_model=self.car_model,
            engine_type="petrol",
            engine_size=2.0,
            horsepower=200,
            torque=300,
            transmission="automatic",
            acceleration=7.5,
            top_speed=220,
            fuel_consumption=8.5,
            weight=1500,
            length=4800,
            width=1800,
            height=1400
        )

    def test_get_car_models(self):
        url = reverse('carmodel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_compare_cars(self):
        # Create another car for comparison
        car_model2 = CarModel.objects.create(
            brand=self.brand,
            name="Test Model 2",
            year=2023,
            body_type="SUV"
        )
        
        CarDetails.objects.create(
            car_model=car_model2,
            engine_type="diesel",
            engine_size=2.5,
            horsepower=250,
            torque=400,
            transmission="automatic",
            acceleration=6.5,
            top_speed=230,
            fuel_consumption=7.5,
            weight=1800,
            length=4900,
            width=1900,
            height=1700
        )

        url = reverse('compare-list')
        data = {
            'car_model_ids': [self.car_model.id, car_model2.id]
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['cars']), 2)
        self.assertIn('comparison', response.data)
        self.assertIn('horsepower', response.data['comparison'])
