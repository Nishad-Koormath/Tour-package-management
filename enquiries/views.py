from django.shortcuts import render
from rest_framework import viewsets
from .models import Enquiry
from .serializers import EnquirySerializer
from .permissions import EnquiryPermission

# Create your views here.
class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [EnquiryPermission]
