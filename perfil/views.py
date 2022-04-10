from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

#Models
from .models import Project

# Create your views here.
def profile(request):
    
    # p1 = Project(title = "Curso de Html", desc = "Descripción de Html")
    # p1.save()
    
    # p2 = Project(title = "Curso de Css", desc = "Descripción de Css")
    # p2.save()
    
    # p3 = Project(title = "Curso de Django", desc = "Descripción de Django")
    # p3.save()
    
    projects = Project.objects.all()

    return HttpResponse(projects);
