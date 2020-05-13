from django.urls import path
from dcp_api.views import patientListView

urlpatterns = [
    path('',patientListView.as_view(), name='list'),
]
