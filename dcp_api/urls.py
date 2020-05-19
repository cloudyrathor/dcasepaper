from django.urls import path
from dcp_api.views import *

urlpatterns = [
    path('patients/',PostPatients.as_view(), name='list'),   
    path('patients/<int:p_id>/',PostPatient.as_view(), name ='member' ),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:emonth>/<slug:slug>/', views.article_detail),
]