import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dcp_project.settings')
import django
django.setup()

from dcp_api.models import pat_profile_table,med_profile_table,pat_treatment_history_table,treatment_plan_table



from faker import Faker
from random import *
fake = Faker()
# fake = Faker(['hi_IN'])

def phonenumbergen():
    p = randint(7,9)
    pno = ''+str(p)
    for i in range(9):
        pno = pno + str(randint(0,9))
    return str(pno)

def populate(n):
    for i in range(n):
        pat_id = fake.random_int(min=1,max=999)
        pat_name = fake.name()
        pat_dob = fake.date()
        pat_address = fake.address()
        pat_email = fake.address()
        pat_mobile = phonenumbergen()
        pat_anniversary = fake.date()
        pat_habbit = fake.random_element(elements = ('Nail biting','Brushing hard','Grinding','chewing ice cube','constant snaking','using teeth as tool'))
        pat_level_of_higgins = fake.random_element(elements = ('Proper brushing','Flossing','Avoid Tobacco','Limit Sodas','Limit Coffee','Limit Alcohol','Consume Calsium','Regular Mouth wash'))
        pat_cosmetic_concern = fake.random_element(elements = ('Teeth whitening','Bonding','Veneers','Crowns','Enamel Shaping and contouring','Braces','Bridges','Implant'))
        pat_medical_history = fake.random_element(elements = ('Cardiovascular','Respiratory','Gastrointestinal','Hepatic','Neurological','Musculoskeletal','Drug history','Allergy'))
        doc_id = fake.random_int(min=1,max=20)
        doc_id_treated_by = doc_id
        treatment_id = fake.random_int(min=1,max=99)
        visit_date = fake.date()
        observations = fake.random_element(elements = ('type1_observation','type2_observation','type3_observation','type4_observation','type5_observation'))
        treatment_amount = fake.random_int(min=350,max=9999)
        treatment_name = fake.random_element(elements = ('Teeth whitening','Bonding','Veneers','Crowns','Enamel Shaping and contouring','Braces','Bridges','Implant'))
        # =====================pat_profile_table================================================================================================
        pat_profile_table_data = pat_profile_table.objects.get_or_create(p_id = pat_id,
                                                           p_name = pat_name,
                                                           p_dob = pat_dob,
                                                           p_address = pat_address,
                                                           p_email = pat_email,
                                                           p_mobile = pat_mobile,
                                                           p_anniversary = pat_anniversary)
        # =======================================================================================================================

        # =====================med_profile_table=================================================================================
        med_profile_table_data = med_profile_table.objects.get_or_create(p_id=pat_id,
                                                                         p_habbit=pat_habbit,
                                                                         p_level_of_higgins=pat_level_of_higgins,
                                                                         p_cosmetic_concern=pat_cosmetic_concern,
                                                                         p_medical_history=pat_medical_history)

        # =======================================================================================================================

        # =====================pat_treatment_history_table================================================================================================
        pat_treatment_history_table_data = pat_treatment_history_table.objects.get_or_create(p_id=pat_id,
                                                                         d_id_treated_by=doc_id_treated_by,
                                                                         treatment_id=treatment_id,
                                                                         visit_date=visit_date,
                                                                         observations=observations,
                                                                         treatment_amount=treatment_amount)
        # =======================================================================================================================

        # =====================treatment_plan_table================================================================================================
        treatment_plan_table_data = treatment_plan_table.objects.get_or_create(t_id=treatment_id,
                                                                         d_id=doc_id,
                                                                         treatment_name=treatment_name,
                                                                         treatment_amount=treatment_amount)
        # =======================================================================================================================


populate(100)



