from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
 
   
    path('<name>/', about,name='about'),
    path('service-details/<id>', service_details , name = 'service_details' ),
    path('project-details/<id>', project_details , name = 'project_details' ),
    path('<name>/about', about,name='about'),
    path('<name>/resume', resume,name='resume'),
    path('<name>/skill', skill, name='skill'),
    path('<name>/projects', projects,name='projects'),
    path('<name>/services', services,name='services'),
    path('<name>/contact', contact,name='contact'),
]
