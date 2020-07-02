from rest_framework import generics
from dcp_api.models import * 
from dcp_api.Serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend

class Post_Patients(generics.ListCreateAPIView):#Patient #Single object insert + GET(List of Object's)
    queryset = pat_profile_table.objects.all()
    serializer_class = pat_profile_tableSerializer
    
class RUD_Patient(generics.RetrieveUpdateDestroyAPIView):#Patient #Single object GET + Update (PUT) + Delete
    queryset = pat_profile_table.objects.all()
    serializer_class = pat_profile_tableSerializer
   #lookup_field = 'p_id'

class Post_PatientMedProfile(generics.CreateAPIView):#Patient_Med_Profile #Single object insert
    queryset = med_profile_table.objects.all()
    serializer_class = med_profile_tableSerializer
    
class RUD_PatientMedProfile(generics.RetrieveUpdateDestroyAPIView): #Patient_Med_Profile #Single object GET + Update (PUT) + Delete
    queryset = med_profile_table.objects.all()
    serializer_class = med_profile_tableSerializer
    lookup_field = 'p_id'

class Post_Doctors(generics.ListCreateAPIView):#Doctor #Single object insert + GET(List of Object's)
    queryset = doc_profile_table.objects.all()
    serializer_class = doc_profile_tableSerializer
    
class RUD_Doctors(generics.RetrieveUpdateDestroyAPIView):#Doctor #Single object GET + Update (PUT) + Delete
    queryset = doc_profile_table.objects.all()
    serializer_class = doc_profile_tableSerializer
   #lookup_field = 'p_id'

class Post_Treatment(generics.ListCreateAPIView):#Doctor #Single object insert + GET(List of Object's)
    queryset = treatment_plan_table.objects.all()
    serializer_class = treatment_plan_tableSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','d_id' )

class RUD_Treatment(generics.RetrieveUpdateDestroyAPIView):#Doctor #Single object GET + Update (PUT) + Delete
    queryset = treatment_plan_table.objects.all()
    serializer_class = treatment_plan_tableSerializer
    
class Post_Patient_Treatment_History(generics.ListCreateAPIView):#Patient_History #Single object insert Done + GET(List of Object's for p_id)
    queryset = PatientTreatmentWorkdone.objects.all()
    serializer_class = pat_treatment_history_tableSerializer
   
    filter_backends = (DjangoFilterBackend,OrderingFilter,)
    ordering = ('visit_date',)
    filter_fields = ('p_id','d_id','t_id','d__d_name')

    .

# class RUD_Patient_Treatment_History(generics.RetrieveUpdateDestroyAPIView):#Patient_History #Single object GET + Update (PUT) + Delete
#     queryset = pat_treatment_history_table.objects.all()
#     serializer_class = pat_treatment_history_tableSerializer
#     lookup_field = ['id','p_id'] 



