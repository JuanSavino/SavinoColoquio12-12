# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.models import Alumno

from django.shortcuts import render

# Create your views here.

def dame_nombres(request):
    context = {}
    context['Alumnos'] = Alumno.objects.all()
    return render(request, 'index.html', context)

