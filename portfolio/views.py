from django.shortcuts import render
from .models import Education, Skill, Project, Certification

def home(request):
    educations = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'educations': educations,
        'skills': skills,
        'projects': projects,
        'certifications': certifications,
    }
    return render(request, 'portfolio/home.html', context)
