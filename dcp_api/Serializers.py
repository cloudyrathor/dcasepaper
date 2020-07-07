from rest_framework import serializers 
from .models import *

class PatientMedicalProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PatientMedicalProfile
        fields = ['id',
                  'Patient',
                  'P_habbit',
                  'P_level_of_higgins',
                  'P_cosmetic_concern',
                  'P_medical_history']    
        read_only_fields = ('Patient',)          
     
class PatientProfileSerializer(serializers.ModelSerializer):

    MedicalProfile = PatientMedicalProfileSerializer(many=True)

    class Meta:
        model = PatientProfile
        fields = ['id',
                  'P_Name',
                  'P_DOB',
                  'P_Address',
                  'P_Email',
                  'P_Mobile',
                  'P_Religion',
                  'P_Gender',
                  'P_Family',
                  'P_MaritalStatus',
                  'P_Anniversary',
                  'MedicalProfile']

    def create(self,validated_data):
        medicalprofiles = validated_data.pop('MedicalProfile')
        Patient = PatientProfile.objects.create(**validated_data)
        for medicalprofile in medicalprofiles:
            PatientMedicalProfile.objects.create(Patient=Patient, **medicalprofile)
        return Patient

    def update(self, instance, validated_data):

        medicalprofiles = validated_data.pop('MedicalProfile')
        instance.P_Name = validated_data.get('P_Name', instance.P_Name) 
        instance.save()

        keep_medicalprofiles = []
        existing_ids = [mp.id for mp in instance.MedicalProfile]
        for medicalprofile in medicalprofiles:
            if "id" in medicalprofile.keys():
                if PatientMedicalProfile.objects.filter(id=medicalprofile["id"]).exists():
                    mp = PatientMedicalProfile.objects.get(id=medicalprofile["id"])
                    mp.P_habbit = medicalprofile.get('P_habbit', mp.P_habbit)
                    mp.save()
                    keep_medicalprofiles.append(mp.id)
                else:
                    continue
            else:
                mp = PatientMedicalProfile.create(**medicalprofile, Patient=instance)
                keep_medicalprofiles.append(mp.id)

        for medicalprofile in instance.MedicalProfile:
            if medicalprofile.id not in keep_medicalprofiles:
                medicalprofile.delete()

        return instance        

class DoctorProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class DoctorClinicSerializer(serializers.ModelSerializer):
    
    Doctor = DoctorProfileSerializer(read_only=True) 

    class Meta:
        model = DoctorClinic
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


