from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, TestimonialViewSet, home
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
