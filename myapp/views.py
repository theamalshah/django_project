# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import user
from django.shortcuts import render

# Create your views here.
def home(request):
	data=user.objects.all();
	return render(request,"myapp/home.html",{"data":data})