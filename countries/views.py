from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, City
from .serializers import CountrySerializer, CitySerializer

# Create your views here.

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CitySerializer
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer