from django.shortcuts import render

from .models import *


# Create your views here.




def about(request , name):
    user = User.objects.get(username=name)
    about_me = About.objects.get(user = user)
    profile = Profile.objects.get(user = user)
    skills = Skill.objects.filter(user = user)
    context = {'about_me':about_me, 'profile':profile, 'skills':skills}
    return render(request , 'about.html',context)

def skill(request , name):
    user = User.objects.get(username=name)
    skills = Skill.objects.filter(user = user)
    context = {'skills':skills}
    return render(request , 'skill.html',context)


def resume(request , name):
    user = User.objects.get(username=name)
    about_me = About.objects.get(user = user)
    my_summary = Summary.objects.get(user= user)
    my_education = Education.objects.filter(user= user)
    my_experience = ProfessionaExperience.objects.filter(user= user)
    context = {'about_me':about_me, 'my_summary':my_summary , 'my_education':my_education , 'my_experience': my_experience}
    return render(request , 'resume.html',context)


def projects(request , name):
    user = User.objects.get(username=name)
    about_me = About.objects.get(user = user)
    project = Project.objects.filter(user = user)
    context = {'about_me':about_me, 'project':project}
    return render(request , 'projects.html',context)


def services(request , name):
    user = User.objects.get(username=name)
    about_me = About.objects.get(user = user)
    my_service = Service.objects.filter(user = user)
    context = {'about_me':about_me , 'my_service':my_service}
    return render(request , 'services.html',context)

def contact(request, name):
    user = User.objects.get(username=name)
    profile = Profile.objects.get(user = user)
    context = {'profile':profile}
    return render(request , 'contact.html',context)

def service_details(request,id):
    service_id = Service.objects.get( id = id )
    context = {'service_id': service_id}
    return render ( request , 'service_details.html', context )

def project_details(request,id):
    project_id = Project.objects.get( id = id )
    context = {'project_id': project_id}
    return render ( request , 'project_details.html', context )