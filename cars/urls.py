from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'brands', views.BrandViewSet)
router.register(r'models', views.CarModelViewSet)
router.register(r'details', views.CarDetailsViewSet, basename='details')
router.register(r'compare', views.CompareViewSet, basename='compare')

urlpatterns = [
    path('', include(router.urls)),
] 