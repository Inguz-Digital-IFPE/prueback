from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class UserProfile(AbstractBaseUser):
    USERNAME_FIELD = 'nombre'

    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='Uprofile'
    )

    nombre = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    apellidos = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    curp = models.CharField(max_length=64, blank=True, null=True)

    fecha_nacimiento = models.DateField(null=True, blank=True)

    edad = models.IntegerField(blank=True, null=True)
