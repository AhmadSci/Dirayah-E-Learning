from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from home.models import UserProfile

# Create your views here.

def user_profile(request, username):
    if request.user.is_authenticated:
        try:
            req_user = User.objects.get(username=username)
            req_profile = UserProfile.objects.get(user=req_user)
        except:
            req_user = None
            req_profile = None

        if req_user is None:
            return render(request,'coderprofile/profilepage.html', context={
                "user": None,
                'profile': None
            })
        else:
            return render(request,'coderprofile/profilepage.html', context={
                "user": req_user,
                'profile': req_profile
            })
    else:
        return redirect('login')

def my_profile(request):
    if request.user.is_authenticated:
        return user_profile(request, request.user.username)
    else:
        return redirect('login')