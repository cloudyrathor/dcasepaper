from django.urls import path
from dcp_api.views import *

urlpatterns = [
    



    #-----------Patient with Nested Medical Profile-------------
    path('patient-with-medical-profile/',PatientAndMedicalProfileListView.as_view(), name='patient-with-medical-profile-list'),
    path('patient-with-medical-profile/<int:pk>',RUD_PatientAndMedicalProfile.as_view(), name='patient-with-medical-profile'),
    #-----------Patient with Nested Medical Profile-------------

    #-----------Work Done Logs-------------
    path('Work-Done-Log/',WorkDoneLogListView.as_view(), name='work-done-log-list'),
    #-----------End Work Done Logs-------------


    # path('patient-profile-list/',Post_Patients.as_view(), name='patient-profile-list'),   
    # path('patient-profile/<int:pk>/',RUD_Patient.as_view(), name ='patient-profile' ),

    # path('patient-medical-post/',Post_PatientMedProfile.as_view(), name='patient-medical-post'),   
    # path('patient-medical-profile/<int:p_id>/',RUD_PatientMedProfile.as_view(), name ='patient-medical-profile' ),

    # path('doctor-profile-list/',Post_Doctors.as_view(), name='doctor-profile-list'),
    # path('doctor-profile/<int:pk>/',RUD_Doctors.as_view(), name ='doctor-profile'),

    # path('treatment-new/',Post_Treatment.as_view(), name='treatment-new'),
    # path('treatment',RUD_Treatment.as_view(), name ='treatment'),

    #In_Process

    #path('patient-treatment-history/',Post_Patient_Treatment_History.as_view(), name='patient-treatment-history'),
    #path('patient-treatment-history/<int:pk>/<int:p_id>',RUD_Patient_Treatment_History.as_view(), name ='patient-treatment-history'),
    
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:emonth>/<slug:slug>/', views.article_detail),

]
