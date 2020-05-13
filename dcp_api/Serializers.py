from rest_framework import serializers 
from .models import pat_profile_table
from .models import pat_treatment_history_table
 
class pat_profile_tableSerializer(serializers.ModelSerializer):

    class Meta:
        model = pat_profile_table
        fields = '__all__'

class pat_treatment_history_tableSerializer(serializers.ModelSerializer):

    class Meta:
        model = pat_treatment_history_table
        fields = '__all__'

