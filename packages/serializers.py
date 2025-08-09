from rest_framework import serializers
from  packages.models import TourPackage, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class TourPackageSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)
    
    destination_city_name = serializers.CharField(source='destination_city.name', read_only=True)
    source_city_name = serializers.CharField(source='source_city.name', read_only=True)
    destination_country_name = serializers.CharField(source='destination_country.name', read_only=True)
    source_country_name = serializers.CharField(source='source_country.name', read_only=True)
    
    class Meta:
        model = TourPackage
        fields = '__all__'