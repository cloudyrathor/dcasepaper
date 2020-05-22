from django.db import models

# Create your models here.
class pat_profile_table(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=64)
    p_dob = models.DateField()
    p_address = models.CharField(max_length=128)
    p_email = models.EmailField()
    p_mobile = models.CharField(max_length=10)
    p_anniversary = models.DateField()
    class Meta:
      managed = False

class med_profile_table(models.Model):
    p_id = models.ForeignKey(pat_profile_table ,on_delete=models.CASCADE) 
    p_habbit = models.CharField(max_length=128)
    p_level_of_higgins = models.CharField(max_length=64)
    p_cosmetic_concern = models.CharField(max_length=128)
    p_medical_history = models.CharField(max_length=1024)
    class Meta:
      managed = False

class pat_treatment_history_table(models.Model):
    p_id = models.IntegerField()
    d_id_treated_by = models.CharField(max_length=64)
    treatment_id = models.IntegerField()
    visit_date = models.DateField()
    observations = models.CharField(max_length=64)
    treatment_amount = models.IntegerField()

class treatment_plan_table(models.Model):
    t_id = models.IntegerField()
    d_id = models.IntegerField()
    treatment_name = models.CharField(max_length=128)
    treatment_amount = models.IntegerField()

