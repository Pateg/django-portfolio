import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from projects.models import Project, Skill

projects = [
    {"title": "School Management System", "slug": "school-management-system", "short_description": "Helps schools manage fees, students and results.", "description": "A complete school management system built with Django and Bootstrap. Schools can manage students, fees, results, and records in one place.", "category": "web", "tags": "Django, Bootstrap, Python"},
    {"title": "E-commerce Website", "slug": "ecommerce-website", "short_description": "Online business - sell products online.", "description": "A full e-commerce website for online business. Product listings, cart, and order enquiries built with Django and Bootstrap.", "category": "web", "tags": "Django, Bootstrap, Python"},
    {"title": "Fashion Boutique", "slug": "fashion-boutique", "short_description": "Product presentation, WhatsApp ordering and contact info.", "description": "A fashion boutique website showing product presentation, WhatsApp ordering and contact information for easy customer enquiries.", "category": "web", "tags": "Django, Bootstrap, Python"},
    {"title": "Beauty Salon", "slug": "beauty-salon", "short_description": "Shows services, pricing, photographs and appointment enquiries.", "description": "A beauty salon website showing services, pricing, photographs and appointment enquiries.", "category": "web", "tags": "Django, Bootstrap, Python"},
    {"title": "Food and Catering", "slug": "food-and-catering", "short_description": "Show menu, food images and order enquiries.", "description": "A food and catering website to show menu, food images and order enquiries via WhatsApp.", "category": "web", "tags": "Django, Bootstrap, Python"},
    {"title": "Real Estate", "slug": "real-estate", "short_description": "Show property listings, location and enquiry forms.", "description": "A real estate website showing property listings, location and enquiry forms for potential buyers and renters.", "category": "web", "tags": "Django, Bootstrap, Python"},
]

for p in projects:
    Project.objects.update_or_create(slug=p['slug'], defaults={**p, 'featured': True})

skills = [
    {"name": "Python", "level": 90, "icon": "🐍"},
    {"name": "Django", "level": 85, "icon": "🎯"},
    {"name": "HTML/CSS", "level": 90, "icon": "🎨"},
    {"name": "JavaScript", "level": 70, "icon": "⚡"},
    {"name": "Bootstrap", "level": 85, "icon": "💅"},
]

for s in skills:
    Skill.objects.update_or_create(name=s['name'], defaults=s)

print("DONE - 6 projects + 5 skills added!")
