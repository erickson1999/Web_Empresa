from django.shortcuts import render
from .models import Project
# Create your views here.

def blog(request):
    proyectos=Project.objects.all()
    return render(request,'core/blog.html',{'proyectos':proyectos})
