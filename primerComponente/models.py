from datetime import datetime
from django.utils import timezone
from django.db import models

# Create your models here.


class PrimerModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

class SegundoModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'segundo_modelo'

