from django.db import models
from account.models import User

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = (
            ('admin_things', 'All thing that admin can do'),
        )

    def __str__(self):
        return self.user.first_name

# Create your models here.
