from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UpdateUserForm, UpdateUserProfile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

@login_required
def user_profile(request):
    if request.method == "POST":
        p_form = UpdateUserProfile(request.POST, request.FILES, instance=request.user.profile)
        u_form = UpdateUserForm(request.POST, instance=request.user)
        
        if p_form.is_valid and u_form.is_valid:
            p_form.save()
            u_form.save()
            
            messages.success(request, "Profile Updated Successfully")
            return redirect("users-profile")
    else:
        p_form = UpdateUserProfile(instance=request.user.profile)
        u_form = UpdateUserForm(instance=request.user)
    context = {
        "p_form": p_form,
        "u_form": u_form
    }
    return render(request, "users/profile.html", context)