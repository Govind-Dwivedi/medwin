from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, password, is_staff, is_superuser, is_patient, is_doctor, is_administrator):
        if not email:
            raise ValueError("Email is required!")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            is_patient = is_patient,
            is_doctor = is_doctor,
            is_administrator = is_administrator
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None):
        user = self._create_user(email, first_name, last_name, password, False, False, True, False, False)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self._create_user(email, first_name, last_name, password, True, True, True, False, True)

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def get_email(self):
        return self.email

# Create your models here.