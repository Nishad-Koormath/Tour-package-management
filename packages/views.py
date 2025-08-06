from django.shortcuts import render
from rest_framework import viewsets
from .models import TourPackage, Schedule
from .serializers import TourPackageSerializer, ScheduleSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminOrReadOnly]