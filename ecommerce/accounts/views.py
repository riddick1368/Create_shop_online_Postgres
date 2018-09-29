from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else :
            messages.error(request,"Bad username or password")

    return render(request,"login.html",context={})



def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
