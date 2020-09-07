from rest_framework import generics
from dcp_api.models import *
from dcp_api.Serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_bulk import (
  ListBulkCreateUpdateDestroyAPIView
)

# class Post_Patients(generics.ListCreateAPIView):#Patient #Single object insert + GET(List of Object's)
#     queryset = pat_profile_table.objects.all()
#     serializer_class = pat_profile_tableSerializer

# class RUD_Patient(generics.RetrieveUpdateDestroyAPIView):#Patient #Single object GET + Update (PUT) + Delete
#     queryset = pat_profile_table.objects.all()
#     serializer_class = pat_profile_tableSerializer
#    #lookup_field = 'p_id'

# class Post_PatientMedProfile(generics.CreateAPIView):#Patient_Med_Profile #Single object insert
#     queryset = med_profile_table.objects.all()
#     serializer_class = med_profile_tableSerializer

# class RUD_PatientMedProfile(generics.RetrieveUpdateDestroyAPIView): #Patient_Med_Profile #Single object GET + Update (PUT) + Delete
#     queryset = med_profile_table.objects.all()
#     serializer_class = med_profile_tableSerializer
#     lookup_field = 'p_id'

# class Post_Doctors(generics.ListCreateAPIView):#Doctor #Single object insert + GET(List of Object's)
#     queryset = doc_profile_table.objects.all()
#     serializer_class = doc_profile_tableSerializer

# class RUD_Doctors(generics.RetrieveUpdateDestroyAPIView):#Doctor #Single object GET + Update (PUT) + Delete
#     queryset = doc_profile_table.objects.all()
#     serializer_class = doc_profile_tableSerializer
#    #lookup_field = 'p_id'

# class Post_Treatment(generics.ListCreateAPIView):#Doctor #Single object insert + GET(List of Object's)
#     queryset = treatment_plan_table.objects.all()
#     serializer_class = treatment_plan_tableSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('id','d_id' )

# class RUD_Treatment(generics.RetrieveUpdateDestroyAPIView):#Doctor #Single object GET + Update (PUT) + Delete
#     queryset = treatment_plan_table.objects.all()
#     serializer_class = treatment_plan_tableSerializer

# class Post_Patient_Treatment_History(generics.ListCreateAPIView):#Patient_History #Single object insert Done + GET(List of Object's for p_id)
#     queryset = PatientTreatmentWorkdone.objects.all()
#     serializer_class = pat_treatment_history_tableSerializer

#     filter_backends = (DjangoFilterBackend,OrderingFilter,)
#     ordering = ('visit_date',)
#     filter_fields = ('p_id','d_id','t_id','d__d_name')

# # class RUD_Patient_Treatment_History(generics.RetrieveUpdateDestroyAPIView):#Patient_History #Single object GET + Update (PUT) + Delete
# #     queryset = pat_treatment_history_table.objects.all()
# #     serializer_class = pat_treatment_history_tableSerializer
# #     lookup_field = ['id','p_id']


#--------------------------Patient Model API classes (List And CRUD)---------------------------------
class PatientProfileListView(generics.ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    

class RUD_PatientProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
#--------------------------End Patient Model API classes (List And CRUD)------------------------------


#--------------------------Patient Medical Profile Model API classes------------------
class PatientMedicalProfileListView(generics.ListCreateAPIView):
    queryset = PatientMedicalProfile.objects.all()
    serializer_class = PatientMedicalProfileSerializer

class RUD_PatientMedicalProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientMedicalProfile.objects.all()
    serializer_class = PatientMedicalProfileSerializer
    lookup_field = 'p_id'
#--------------------------Patient Medical Profile Model API classes------------------


#-------------------------PatientAndMedicalProfile Nested Data List And CRUD-------------
class PatientAndMedicalProfileListView(generics.ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientAndMedicalProfileSerializer

class RUD_PatientAndMedicalProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientAndMedicalProfileSerializer
#-------------------------END PatientAndMedicalProfile Nested Data List And CRUD-------------


#--------------------------Doctor Profile Model API classes---------------------------
class DoctorProfileListView(generics.ListCreateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

class RUD_DoctorProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
#--------------------------End Doctor Profile Model API classes-------------------------


#--------------------------Visit Model API Classes------------------------------
class VisitsListView(generics.ListCreateAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','Patient__id')

class RUD_Visits(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer
#--------------------------End Visit Model API Classes------------------------------


#--------------------------Complaint Model API classes (List And CRUD)---------------------
class ComplaintsListView(generics.ListCreateAPIView):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','Patient__id')

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(ComplaintsListView, self).list(request, *args, **kwargs)
        # customize the response data
        # response.data = {"people": response.data}
        # return response with this custom representation

        Patient_data = []
        Doctor_data = []
      
        for row in response.data:
            Patient_data.append(row.pop('Patient'))
            Doctor_data.append(row.pop('Doctor'))
            
           # print(Treatment_data)

        Patient = [i for n, i in enumerate(Patient_data) if i not in Patient_data[n + 1:]]
        Doctor = [i for n, i in enumerate(Doctor_data) if i not in Doctor_data[n + 1:]]
     
        # print(Patient)
        # print(Doctor)
        # print(Visits)

        response.data = {"Complaints":{"Patient":Patient[0],"Doctor":Doctor[0],"Complaint_Array":response.data}}
        return response


class RUD_Complaints(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer
#--------------------------End Complaint Model API classes (List And CRUD)------------------------------

#--------------------------Work Done Log Model API Classes------------------------------
#-----------------Work Done Log Post And List (Bulk POST And Update)--------------------
class WorkDoneLogListView(ListBulkCreateUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset = WorkDoneLog.objects.all()
    serializer_class = WorkDoneLogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','Patient__id','Complaint__id','Visits__id')

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(WorkDoneLogListView, self).list(request, *args, **kwargs)
        # customize the response data

        # response.data = {"people": response.data}
        # return response with this custom representation

        Patient_data = []
        Doctor_data = []
        Visit_data = []
        Complaint_data = []
        WorkDone_Time_Stamp_data = []
        Treatment_data = []
        for row in response.data:
            Patient_data.append(row.pop('Patient'))
            Doctor_data.append(row.pop('Doctor'))
            Visit_data.append(row.pop('Visits'))
            Complaint_data.append(row.pop('Complaint'))
            WorkDone_Time_Stamp_data.append(row.pop('WorkDone_Time_Stamp'))
            Treatment_data.append(row.pop('Treatment'))
            print(WorkDone_Time_Stamp_data)
            
           # print(Treatment_data)

        Patient = [i for n, i in enumerate(Patient_data) if i not in Patient_data[n + 1:]]
        Doctor = [i for n, i in enumerate(Doctor_data) if i not in Doctor_data[n + 1:]]
        Visits = [i for n, i in enumerate(Visit_data) if i not in Visit_data[n + 1:]]
        Complaint = [i for n, i in enumerate(Complaint_data) if i not in Complaint_data[n + 1:]] 
        WorkDone_Time_Stamp = [i for n, i in enumerate(WorkDone_Time_Stamp_data) if i not in WorkDone_Time_Stamp_data[n + 1:]]
        # print(Doctor)
        # print(Visits)

        response.data = {"WorkDone":{"Patient":Patient[0],"Doctor":Doctor[0],"Visits":Visits[0],"Complaint":Complaint[0],"WDate":{WorkDone_Time_Stamp[0]:Treatment_data}}}
        return response

#--------------------------Work Done Log Single CRUD..........................................
class RUD_WorkDoneLog(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkDoneLog.objects.all()
    serializer_class = WorkDoneLogSerializer
#--------------------------End Work Done Log Model API Classes--------------------------------
#--------------------------Prescription Model API classes (List And CRUD)---------------------
class PrescriptionListView(ListBulkCreateUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','Visit__id','Patient__id')

    def list(self, request, *args, **kwargs):
            # call the original 'list' to get the original response
            response = super(PrescriptionListView, self).list(request, *args, **kwargs)
            # customize the response data
            # response.data = {"people": response.data}
            # return response with this custom representation
            Patient_data = []
            Doctor_data = []
        
            for row in response.data:
                Patient_data.append(row.pop('Patient'))
                Doctor_data.append(row.pop('Visit'))    

            Patient = [i for n, i in enumerate(Patient_data) if i not in Patient_data[n + 1:]]
            Doctor = [i for n, i in enumerate(Doctor_data) if i not in Doctor_data[n + 1:]]
        
            response.data = {"Prescription":{"Patient":Patient[0],"Doctor":Doctor[0].get('Doctor'),"Prescription_data":response.data}}
            return response

class RUD_Prescription(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
#--------------------------End Prescription Model API classes (List And CRUD)------------------
