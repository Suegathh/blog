from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here

def home(request):
    
    posts = Post.objects.all().order_by("-date_created")
    print(posts)
    
    context = {
        "posts" : posts,
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
