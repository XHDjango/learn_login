from django.shortcuts import render, redirect


def index(request):
    return render(request, "login/index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return redirect("/index/")
    return render(request, "login/login.html")


def register(request):
    return render(request, "login/register.html")


def logout(request):
    return redirect("/login/")
