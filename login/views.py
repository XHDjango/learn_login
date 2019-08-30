from django.shortcuts import render, redirect

from . import models


def index(request):
    return render(request, "login/index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = models.User.objects.get(name=username)
        except:
            return render(request, "login/login.html")
        if user.password == password:
            return redirect("/index/")
    return render(request, "login/login.html")


def register(request):
    return render(request, "login/register.html")


def logout(request):
    return redirect("/login/")
