from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'test_app/home.html')

def about(request):
    return render(request, 'test_app/about.html')

def projects(request):
    return render(request, 'test_app/projects.html')

def contact(request):
    return render(request, 'test_app/contact.html')