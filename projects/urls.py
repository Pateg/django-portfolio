from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, TestimonialViewSet, home

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
