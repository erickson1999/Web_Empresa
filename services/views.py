from django.shortcuts import render
from .models import Project
# Create your views here.


def services(request):
    proyectos=Project.objects.all()
    return render(request,'core/services.html',{'proyectos':proyectos})
