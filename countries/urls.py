from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet

router = DefaultRouter()
router.register(r"cities", CityViewSet)
router.register(r'', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]