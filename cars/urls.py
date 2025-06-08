from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CarModelViewSet, CarDetailsViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'models', CarModelViewSet)
router.register(r'details', CarDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 