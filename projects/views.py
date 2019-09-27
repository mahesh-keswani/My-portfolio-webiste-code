from django.shortcuts import render, get_object_or_404
from .models import Project 
from django.http import HttpResponse

def homepage(request):
	projects = Project.objects
	
	return render(request, 'projects/home.html', {'projects': projects})

def allprojects(request):
	projects = Project.objects
	
	return render(request, 'projects/allprojects.html', {'projects': projects})

def details(request, project_id):
	project = get_object_or_404(Project,pk=project_id)
	return render(request, 'projects/details.html', {'project':project})

def about(request):
	return render(request, 'projects/about.html')