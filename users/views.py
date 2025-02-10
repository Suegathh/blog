from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"registration successful for {username}")
            return redirect("blog-home")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {'form': form})

def logout_user(request):
    logout(request)
    return render(request, "users/logout.html")
    