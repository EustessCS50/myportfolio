from django.shortcuts import render

# Create your views here.
from . models import Project


def index(request):
    project = Project.objects.all()

    return render(request, 'index.html', context={'project':project})


def projectDetail(request, project_name):
    project = Project.objects.get(name=project_name)
    print(project)
    return render(request, 'portfolio-details.html', context={'project':project})

