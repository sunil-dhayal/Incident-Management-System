from django.urls import path
from . import views

app_name = 'incidents'
urlpatterns = [
    path('create/', views.create_incident, name='create'),
    path('', views.IncidentListView.as_view(), name='incident_list'),
    path('<str:incident_id>/update/', views.update_incident, name='update_incident'),
]
