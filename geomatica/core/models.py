from django.db import models

# Create your models here.

class Hueco(models.Model):
    direccion = models.CharField(max_length=200)
    latitud = models.IntegerField(default=0)
    longitud = models.IntegerField(default=0)
    foto = models.ImageField()

class Trafico(models.Model):
    zona = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
