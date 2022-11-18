from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_home, name="patient_home"),
    path('bookappointment/', views.book_Appointment, name='book_Appointment'),
    path('appointment-history/', views.appointHistory, name='appointHistory'),
]
