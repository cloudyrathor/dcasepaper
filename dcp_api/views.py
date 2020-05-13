from django.shortcuts import render
from dcp_api.models import * 
from dcp_api.Serializers import *
from rest_framework import status
from rest_framework import generics 
from rest_framework.mixins import ListModelMixin


class patientListView(generics.GenericAPIView,ListModelMixin):
    serializer_class = pat_profile_tableSerializer
    queryset = pat_profile_table.objects.all()

# Create your views here test.


