from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser
from . forms import SignupForm, LoginForm


# Create your views here.

# Landing page function

def home(request):
    template_name = 'accounts/index.html'
    if request.method == 'GET':
        context = {

        }
        return render(request, template_name, context)


def signup(request):
    context = {
    }
    template_name = 'accounts/signup.html'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data.get('user_type')
            user = form.save(commit=False)
            if user_type == "is_artist":
                user.is_artist = True
            if user_type == "is_sponsor":
                user.is_sponsor = True
            user.save()
            messages.success(request, "Signup successful")
            return redirect('login')
        form = SignupForm()
        context = {
            "signup_form": form,
            "signup_data": request.POST
        }
        return render(request, template_name, context)
    return render(request, template_name)


def Signin(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successful")
                return redirect('home')
            messages.error(request, "invalid login details")
        messages.error(request, "data invalid")
    form = LoginForm()
    context = {
        "signup_form": form,
        "signup_data": request.POST
    }
    return render(request, template_name, context)