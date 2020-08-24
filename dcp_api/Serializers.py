from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *
from rest_framework_bulk import (BulkListSerializer, BulkSerializerMixin)

class PatientProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PatientProfile
        fields = '__all__'

#------------------------------ Patient Medical Profile Model Serializer------------------------------------------------------
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
#------------------------------End Patient Medical Profile Model Serializer---------------------------------------------------             
#---------------(Create and Update Methods) Patient And Nested Patient Medical Profile Mix Serializer-------------------------
class PatientAndMedicalProfileSerializer(serializers.ModelSerializer):

    MedicalProfile = PatientMedicalProfileSerializer(many=True, read_only=True)

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
                  'MedicalProfile',
                  'Appointment']

    #-----------Create Patient with there medical profile---------
    def create(self,validated_data):
        medicalprofiles = validated_data.pop('MedicalProfile')
        Patient = PatientProfile.objects.create(**validated_data)
        for medicalprofile in medicalprofiles:
            PatientMedicalProfile.objects.create(Patient=Patient, **medicalprofile)
        return Patient

    #-----------Update Patient with there medical profile---------
    def update(self, instance, validated_data):

        medicalprofiles = validated_data.pop('MedicalProfile')
        instance.P_Name = validated_data.get('P_Name', instance.P_Name)     
        instance.P_DOB = validated_data.get('P_DOB', instance.P_DOB) 
        instance.P_Address = validated_data.get('P_Address', instance.P_Address) 
        instance.P_Email = validated_data.get('P_Email', instance.P_Email) 
        instance.P_Mobile = validated_data.get('P_Mobile', instance.P_Mobile) 
        instance.P_Religion = validated_data.get('P_Religion', instance.P_Religion)  
        instance.P_Gender = validated_data.get('P_Gender', instance.P_Gender)  
        instance.P_Family = validated_data.get('P_Family', instance.P_Family)  
        instance.P_MaritalStatus = validated_data.get('P_MaritalStatus', instance.P_MaritalStatus)  
        instance.P_Anniversary = validated_data.get('P_Anniversary', instance.P_Anniversary)  
        instance.save()

        keep_medicalprofiles = []

        existing_ids = [mp.id for mp in instance.MedicalProfile]
        for medicalprofile in medicalprofiles:
            if "id" in medicalprofile.keys():
                if PatientMedicalProfile.objects.filter(id=medicalprofile["id"]).exists():
                    mp = PatientMedicalProfile.objects.get(id=medicalprofile["id"])
                    mp.P_habbit = medicalprofile.get('P_habbit', mp.P_habbit)
                    mp.P_level_of_higgins = medicalprofile.get('P_level_of_higgins', mp.P_level_of_higgins)
                    mp.P_cosmetic_concern = medicalprofile.get('P_cosmetic_concern', mp.P_cosmetic_concern)
                    mp.P_medical_history = medicalprofile.get('P_medical_history', mp.P_medical_history)
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
#---------------End (Create and Update Methods) Patient And Nested Patient Medical Profile Mix Serializer---------------------

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
    Patient_Id = serializers.IntegerField(write_only = True)
    Doctor_Id = serializers.IntegerField(write_only = True)

    class Meta:
        model = Complaints
        fields = ['id','Patient','Doctor','Patient_Id','Doctor_Id','C_TimeStamp','CompaintDetail']

    def create(self, validated_data):
        
        #...........Removing this values
        patient = validated_data.pop('Patient_Id') 
        doctor = validated_data.pop('Doctor_Id')
               
        #...........Geting instance from the respected field table
        patient_instance = PatientProfile.objects.get(id=patient)
        doctor_instance = DoctorProfile.objects.get(id=doctor)
      
        #...........Performin insert operation 
        complaint_instance = WorkDoneLog.objects.create(**validated_data, Patient = patient_instance, Doctor = doctor_instance)        
        return complaint_instance    


class DoctorSpecializationSerializer(serializers.ModelSerializer):

    Doctor = DoctorProfileSerializer(read_only=True)

    class Meta:
        model = DoctorSpecialization
        fields = '__all__'


class VisitsSerializer(serializers.ModelSerializer):                                                                                                                                                                                                               

    Patient = PatientProfileSerializer(read_only=True)
    Doctor = DoctorProfileSerializer(read_only=True)    
    Complaint = ComplaintsSerializer(read_only=True)
    Treatment = DoctorSpecializationSerializer(read_only=True)

    class Meta:
        model = Visits
        fields = '__all__'

#------------------Work Done Log POST-----------------------
#----------------------Bulk Post And Update-----------------
class WorkDoneLogSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    
    #..........Write Only fields for create update  
    Patient_Id = serializers.IntegerField(write_only = True)
    Doctor_Id = serializers.IntegerField(write_only = True)
    Complaint_Id = serializers.IntegerField(write_only = True)
    Treatment_Id = serializers.IntegerField(write_only = True)
    Visit_Id = serializers.IntegerField(write_only = True)
    Details = serializers.CharField(allow_blank=True, max_length=500, required=False)
    Advice = serializers.CharField(allow_blank=True, max_length=500, required=False)
   
    #..........Read_Only for get 
    Patient = SerializerMethodField()
    Doctor = DoctorProfileSerializer(read_only=True)        
    Complaint = ComplaintsSerializer(read_only=True)
    Treatment = DoctorSpecializationSerializer(read_only=True)
    #Visit = VisitsSerializer(read_only=True)

    class Meta:
        model = WorkDoneLog
        list_serializer_class = BulkListSerializer # 
        fields = ['id',
                  'Patient_Id',
                  'Doctor_Id',
                  'Complaint_Id',
                  'Treatment_Id',
                  'Visit_Id',                  
                  'Patient',
                  'Doctor',
                  'Complaint',
                  'Treatment',
                  'Visits',
                  'WorkDone_Time_Stamp',
                  'Details',
                  'Advice']

    def get_Patient(self,obj):
        return str(obj.Patient.P_Name)

    #------------This Method is written for (write_only) field Manupulation------------ 
    def create(self, validated_data):        
        #...........Removing this values
        patient = validated_data.pop('Patient_Id') 
        doctor = validated_data.pop('Doctor_Id')
        complaint = validated_data.pop('Complaint_Id')
        treatment = validated_data.pop('Treatment_Id')
        visit = validated_data.pop('Visit_Id')
        details = validated_data.pop('Details')
        advice = validated_data.pop('Advice')        
        
        #...........Geting instance from the respected field table
        patient_instance = PatientProfile.objects.get(id=patient)
        doctor_instance = DoctorProfile.objects.get(id=doctor)
        complaint_instance = Complaints.objects.get(id=complaint)
        treatment_instance = DoctorSpecialization.objects.get(id=treatment)
                
        try:
            visit_instance = Visits.objects.get(id=visit)        
            visit_instance.Details = details
            visit_instance.Advice = advice                       
            visit_instance.save()

        except Visits.DoesNotExist:
            visit_instance = Visits.objects.create(Patient=patient_instance, Doctor=doctor_instance, Complaint = complaint_instance, Treatment = treatment_instance, Visit_Time_Stamp= validated_data['WorkDone_Time_Stamp'], Details = details, Advice = advice, Visit_Type = "Regular")
                    
        #...........Performin insert operation 
        workdonelog_instance = WorkDoneLog.objects.create(**validated_data, Patient = patient_instance, Doctor = doctor_instance, Complaint = complaint_instance, Treatment = treatment_instance, Visits = visit_instance)
        
        return workdonelog_instance    

#-------------------End Work Done Log POST------------------
class PrescriptionSerializer(serializers.ModelSerializer):

    Patient = PatientProfileSerializer(read_only=True)
    Visit = VisitsSerializer(read_only=True)    
  
    class Meta:
        model = Prescription
        fields = '__all__'


