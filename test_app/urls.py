from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]