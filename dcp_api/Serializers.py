from rest_framework import serializers 
from .models import *
 
class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class DoctorClinicSerializer(serializers.ModelSerializer):
    
    Doctor = DoctorProfileSerializer(read_only=True) 
    class Meta:
        model = DoctorClinic
        fields = '__all__'

class PatientMedicalProfileSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True) 
    class Meta:
        model = PatientMedicalProfile
        fields = '__all__'    
    

class ComplaintsSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True) 
    Doctor = DoctorProfileSerializer(read_only=True)
    class Meta:
        model = Complaints
        fields = '__all__'

class DoctorSpecializationSerializer(serializers.ModelSerializer):

    Doctor = DoctorProfileSerializer(read_only=True)
    class Meta:
        model = DoctorSpecialization
        fields = '__all__'

class WorkDoneLogSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True)
    Doctor = DoctorProfileSerializer(read_only=True)    
    Complaint = ComplaintsSerializer(read_only=True)
    Treatment = DoctorSpecializationSerializer(read_only=True)
    class Meta:
        model = WorkDoneLog
        fields = '__all__'

class VisitsSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True)
    Doctor = DoctorProfileSerializer(read_only=True)    
    Complaint = ComplaintsSerializer(read_only=True)
    Treatment = DoctorSpecializationSerializer(read_only=True)
    class Meta:
        model = Visits
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True)
    Visit = VisitsSerializer(read_only=True)    
  
    class Meta:
        model = Prescription
        fields = '__all__'


