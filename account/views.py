from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def login_request(request):

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            nextUrl = request.GET.get('next', None)

            if nextUrl is None:
                return redirect('index')
            else: 
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html", {
                "error": "Username or password is wrong"
            })

    else:
        return render(request, "account/login.html")

def register_request(request):

    if request.method == 'POST':
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if user.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "This username already exists"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {"error": "This email already exists"})
                else: 
                    User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("index")
        else:
            return render(request, "account/register.html", {"error": "Passwords aren't same"})
        
    else:
        return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("login")
    return render(request, "account/login.html")
