from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.



class Alumno(models.Model):
    name = models.CharField(max_length=50)



class Asistencia(models.Model):
    nombre_alumno= models.CharField(max_length=50)
    datetime = models.DateTimeField('Fecha',auto_now=True)



class Curso(models.Model):
    name = models.CharField(max_length=50)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)


