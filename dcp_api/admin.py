from django.contrib import admin
from dcp_api.models import *

# # Register your models here.
# class pat_profile_tableAdmin(admin.ModelAdmin):
#     list_display = ['id','p_id','p_name','p_dob','p_address','p_email','p_mobile','p_anniversary']

# class med_profile_tableAdmin(admin.ModelAdmin):
#     list_display = ['id','p_id','p_habbit','p_level_of_higgins','p_cosmetic_concern','p_medical_history',]

# class pat_treatment_history_tableAdmin(admin.ModelAdmin):
#     list_display = ['id','p_id','d_id_treated_by','treatment_id','visit_date','observations','treatment_amount',]

# class treatment_plan_tableAdmin(admin.ModelAdmin):
#     list_display = ['id','t_id','d_id','treatment_name','treatment_amount',]

admin.site.register(PatientProfile),
admin.site.register(DoctorProfile),
admin.site.register(DoctorClinic),
admin.site.register(PatientMedicalProfile),
admin.site.register(Complaints),
admin.site.register(DoctorSpecialization),
admin.site.register(WorkDoneLog),
admin.site.register(Visits),
admin.site.register(Prescription)



