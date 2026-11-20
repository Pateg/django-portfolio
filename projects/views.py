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
