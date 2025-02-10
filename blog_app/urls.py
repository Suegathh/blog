from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path("", home, name = 'blog-home'),
    path("about/", about, name = 'blog-about'),
    path("contact/", contact, name = 'blog-contact')
]