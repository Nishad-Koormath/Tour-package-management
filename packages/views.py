from django.shortcuts import render
from rest_framework import viewsets
from .models import TourPackage, Schedule
from .serializers import TourPackageSerializer, ScheduleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer