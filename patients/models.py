from django.db import models
from account.models import User
from doctor.models import Doctor

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doc_comment = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    
# Create your models here.
