from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Service, Project, Experience
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent.")
            return redirect('/#contact')
    else:
        form = ContactForm()

    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'profile': Profile.objects.first(),
        'skills': skills,
        'services': Service.objects.all(),
        'projects': projects,
        'experiences': Experience.objects.all(),
        'project_count': projects.count(),
        'skill_count': skills.count(),
        'form': form,
    }
    return render(request, 'home.html', context)
