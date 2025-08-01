from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourPackageViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet) 
router.register(r'', TourPackageViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
