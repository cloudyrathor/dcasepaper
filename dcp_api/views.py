from django.shortcuts import render
from dcp_api.models import * 
from dcp_api.Serializers import *
from rest_framework import status
from rest_framework import generics 
from rest_framework import mixins


class PostPatients(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    serializer_class = pat_profile_tableSerializer
    queryset = pat_profile_table.objects.all()
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostPatient(mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = pat_profile_table.objects.all()
    serializer_class = pat_profile_tableSerializer
    lookup_field = 'p_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)        


# Create your views here test.


