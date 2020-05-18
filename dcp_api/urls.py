# from django.urls import path
# from dcp_api.views import *

# urlpatterns = [
#     path('patients/',PostPatients.as_view(), name='list'),   
#     path('patients/<int:p_id>/',PostPatient.as_view(), name ='member' ),
#     #path('articles/<int:year>/<int:month>/', views.month_archive),
#     #path('articles/<int:year>/<int:emonth>/<slug:slug>/', views.article_detail),
# ]



from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'patients', PostPatients.as_view()),
#router.register(r'patients', PostPatient.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))    
]