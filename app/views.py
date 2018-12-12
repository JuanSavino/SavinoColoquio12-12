# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models import Alumno
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def dame_alumnos(request):
    context = {}
    context['Alumnos'] = Alumno.objects.all()
    return render(request, 'index.html', context)
    


