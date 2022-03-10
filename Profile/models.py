from django.db import models

# Importaciones de modelos
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    id_user = models.OneToOneField(User, on_delete = models.CASCADE, null=False, blank=False)
    imagen = models.ImageField(null = True, blank = True, default='', upload_to='profile-img/')