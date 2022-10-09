from django.db import models
from account.models import User

class Doctor(models.Model):
    experience = models.IntegerField()
    specialist = models.CharField(max_length=100)
    consultFee = models.IntegerField()
    description = models.CharField(max_length=1000)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
# Create your models here.
