from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import viewsets, filters
from .models import Project, Skill, Testimonial
from .serializers import ProjectSerializer, SkillSerializer, TestimonialSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags', 'category']
    lookup_field = 'slug'

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Message sent! I will reply soon.')
            return redirect('home')

    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Project.objects.values_list('category', flat=True).distinct()
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills,
        'testimonials': testimonials,
        'categories': categories,
    })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # For now we just show success. Later we can email it to you.
        print(f"NEW CONTACT: {name} - {email} - {subject} - {message}")
        messages.success(request, f"Thanks {name}! Your message has been sent. I'll reply to {email} soon.")
        return redirect('contact')
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')
