from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('patientslist/', views.patientsList, name="patientsList"),
    path('doclist/', views.doctorsList, name="doctorsList"),
    path('add_doctor/', views.addDoctor, name="addDoctor"),
    path('remove-doc/', views.removeDoc, name="removeDoc"),
]
