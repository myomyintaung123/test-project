from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def home(request):
    projects = Project.objects.all().order_by('-date_created')  # Get all projects ordered by creation date
    return render(request, 'test_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'test_app/about.html')

def projects(request):
    return render(request, 'test_app/projects.html')

def contact(request):
    return render(request, 'test_app/contact.html')