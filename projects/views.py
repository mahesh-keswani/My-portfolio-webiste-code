from django.shortcuts import render
from .models import Project 
from django.http import HttpResponse

def homepage(request):
	projects = Project.objects
	
	return render(request, 'projects/home.html', {'projects': projects})