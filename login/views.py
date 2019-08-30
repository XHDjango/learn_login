from django.shortcuts import render, redirect

from . import models
from . import forms


def index(request):
    if request.session.get('is_login', None):
        return render(request, "login/index.html")
    return redirect('/login/')


def login(request):
    if request.session.get("is_login", None):
        return redirect("/index/")  # 不允许重复登录
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"

        if login_form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            message = "用户名或密码不匹配!"
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, "login/login.html", locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect("/index/")
            return render(request, "login/login.html", locals())

        return render(request, "login/login.html", locals())

    login_form = forms.UserForm()
    return render(request, "login/login.html", locals())


def register(request):
    return render(request, "login/register.html")


def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()
        return redirect("/login/")
    return redirect("/login/")
