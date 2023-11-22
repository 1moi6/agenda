# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    clinica = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=100, blank=True)
