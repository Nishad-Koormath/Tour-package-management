from rest_framework import serializers
from  packages.models import TourPackage, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class TourPackageSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = TourPackage
        fields = '__all__'