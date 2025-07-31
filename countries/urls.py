from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r"cities", CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]