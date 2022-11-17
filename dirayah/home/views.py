import json
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import NewUserForm, LoginForm
from .models import UserProfile, User

# Create your views here.

# Home Page
def index(request):
    if request.user.is_authenticated:
        answers=UserProfile.objects.get(user=request.user).answers
        recommendations=UserProfile.objects.get(user=request.user).recommendations
        return render(request, 'home/index.html',
        {
            "answers":answers,
            "recommendations":recommendations,
        }
        )
    return render(request, 'home/index.html')

# Authenticate user on login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            username = body["username"]
            password = body["password"]
        except:
            username = request.POST["username"]
            password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "message": "success"
            }) 
        else:
            return JsonResponse({
                "message": "invalid credentials"
            })
    else:
        return render(request, "home/login.html", {"login_form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user).save()
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm() 
    return render (request=request, template_name="home/register.html", context={"register_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")