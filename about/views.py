from django.shortcuts import render
from .models import Project
# Create your views here.

def about(request):
    proyectos=Project.objects.all()
    return render(request,'core/about.html',{'proyectos':proyectos})
