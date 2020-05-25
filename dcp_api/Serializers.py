from rest_framework import serializers 
from .models import *
 
class pat_profile_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = pat_profile_table
        fields = '__all__'

class doc_profile_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_profile_table
        fields = '__all__'       

class treatment_plan_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = treatment_plan_table
        fields = '__all__'             

class med_profile_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_profile_table
        fields = '__all__'

class pat_treatment_history_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = pat_treatment_history_table
        fields = '__all__'

