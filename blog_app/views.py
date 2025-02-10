from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
blogs = [
    {
        "title": "The pet",
        "author": "Sue Jym",
        "date_created": "27-01-2025",
        "content": "adventure"
    },
    {
        "title": "The car",
        "author": "Sue Doe",
        "date_created": "27-01-2024",
        "content": "Cars"
    },
]

def home(request):
    
    context = {
        "blogs" : blogs,
        "title": "Home"
    }
    return render(request, "blog_app/home.html", context)

def about(request):
    context = {
        "title": "About"
    }
    return render(request, "blog_app/about.html")

def contact(request):
   return render(request, "blog_app/contact.html")
