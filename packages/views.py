from django.shortcuts import render
from rest_framework import viewsets
from .models import TourPackage, Schedule
from .serializers import TourPackageSerializer, ScheduleSerializer

# Create your views here.
class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer