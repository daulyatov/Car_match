from django.core.management.base import BaseCommand
from cars.models import Brand, CarModel, CarDetails

class Command(BaseCommand):
    help = 'Loads sample car data for Mercedes-Benz and BMW'

    def handle(self, *args, **kwargs):
        # Create Mercedes-Benz brand
        mercedes = Brand.objects.create(
            name="Mercedes-Benz",
            country="Germany",
            founded_year=1926,
            description="Mercedes-Benz is a German automobile manufacturer known for luxury vehicles, buses, coaches, and trucks."
        )

        # Create BMW brand
        bmw = Brand.objects.create(
            name="BMW",
            country="Germany",
            founded_year=1916,
            description="BMW (Bayerische Motoren Werke) is a German multinational manufacturer of luxury vehicles and motorcycles."
        )

        # Mercedes-Benz models
        mercedes_models = [
            {
                'name': 'S-Class',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 3.0,
                    'horsepower': 429,
                    'torque': 520,
                    'transmission': 'automatic',
                    'acceleration': 4.9,
                    'top_speed': 250,
                    'fuel_consumption': 7.8,
                    'weight': 2070,
                    'length': 5289,
                    'width': 1921,
                    'height': 1503
                }
            },
            {
                'name': 'GLE',
                'year': 2023,
                'body_type': 'SUV',
                'details': {
                    'engine_type': 'petrol',
                    'engine_size': 3.0,
                    'horsepower': 367,
                    'torque': 500,
                    'transmission': 'automatic',
                    'acceleration': 5.7,
                    'top_speed': 250,
                    'fuel_consumption': 9.8,
                    'weight': 2130,
                    'length': 4924,
                    'width': 1947,
                    'height': 1772
                }
            },
            {
                'name': 'C-Class',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 2.0,
                    'horsepower': 204,
                    'torque': 320,
                    'transmission': 'automatic',
                    'acceleration': 7.3,
                    'top_speed': 235,
                    'fuel_consumption': 6.2,
                    'weight': 1685,
                    'length': 4751,
                    'width': 1820,
                    'height': 1437
                }
            },
            {
                'name': 'E-Class',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 2.0,
                    'horsepower': 299,
                    'torque': 400,
                    'transmission': 'automatic',
                    'acceleration': 5.9,
                    'top_speed': 250,
                    'fuel_consumption': 6.8,
                    'weight': 1800,
                    'length': 4942,
                    'width': 1852,
                    'height': 1468
                }
            },
            {
                'name': 'G-Class',
                'year': 2023,
                'body_type': 'SUV',
                'details': {
                    'engine_type': 'petrol',
                    'engine_size': 4.0,
                    'horsepower': 585,
                    'torque': 700,
                    'transmission': 'automatic',
                    'acceleration': 4.5,
                    'top_speed': 240,
                    'fuel_consumption': 14.3,
                    'weight': 2510,
                    'length': 4873,
                    'width': 1984,
                    'height': 1979
                }
            }
        ]

        # BMW models
        bmw_models = [
            {
                'name': '7 Series',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 3.0,
                    'horsepower': 400,
                    'torque': 450,
                    'transmission': 'automatic',
                    'acceleration': 5.1,
                    'top_speed': 250,
                    'fuel_consumption': 7.5,
                    'weight': 2120,
                    'length': 5391,
                    'width': 1950,
                    'height': 1544
                }
            },
            {
                'name': 'X5',
                'year': 2023,
                'body_type': 'SUV',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 3.0,
                    'horsepower': 395,
                    'torque': 600,
                    'transmission': 'automatic',
                    'acceleration': 5.4,
                    'top_speed': 250,
                    'fuel_consumption': 8.9,
                    'weight': 2240,
                    'length': 4930,
                    'width': 2004,
                    'height': 1776
                }
            },
            {
                'name': '3 Series',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'petrol',
                    'engine_size': 2.0,
                    'horsepower': 258,
                    'torque': 400,
                    'transmission': 'automatic',
                    'acceleration': 5.8,
                    'top_speed': 250,
                    'fuel_consumption': 6.8,
                    'weight': 1610,
                    'length': 4709,
                    'width': 1827,
                    'height': 1442
                }
            },
            {
                'name': '5 Series',
                'year': 2023,
                'body_type': 'sedan',
                'details': {
                    'engine_type': 'hybrid',
                    'engine_size': 2.0,
                    'horsepower': 292,
                    'torque': 420,
                    'transmission': 'automatic',
                    'acceleration': 6.1,
                    'top_speed': 235,
                    'fuel_consumption': 7.2,
                    'weight': 1780,
                    'length': 4963,
                    'width': 1868,
                    'height': 1479
                }
            },
            {
                'name': 'X7',
                'year': 2023,
                'body_type': 'SUV',
                'details': {
                    'engine_type': 'petrol',
                    'engine_size': 4.4,
                    'horsepower': 530,
                    'torque': 750,
                    'transmission': 'automatic',
                    'acceleration': 4.7,
                    'top_speed': 250,
                    'fuel_consumption': 12.5,
                    'weight': 2450,
                    'length': 5151,
                    'width': 2000,
                    'height': 1805
                }
            }
        ]

        # Create Mercedes-Benz models and details
        for model_data in mercedes_models:
            details = model_data.pop('details')
            car_model = CarModel.objects.create(brand=mercedes, **model_data)
            CarDetails.objects.create(car_model=car_model, **details)

        # Create BMW models and details
        for model_data in bmw_models:
            details = model_data.pop('details')
            car_model = CarModel.objects.create(brand=bmw, **model_data)
            CarDetails.objects.create(car_model=car_model, **details)

        self.stdout.write(self.style.SUCCESS('Successfully loaded car data')) 