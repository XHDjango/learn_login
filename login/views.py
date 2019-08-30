import hashlib

from django.shortcuts import render, redirect

from . import forms
from . import models


def _hash_code(s, salt="login"):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    if request.session.get("is_login", None):
        return render(request, "login/index.html")
    return redirect("/login/")


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

            if user.password == _hash_code(password):
                request.session["is_login"] = True
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                return redirect("/index/")
            return render(request, "login/login.html", locals())

        return render(request, "login/login.html", locals())

    login_form = forms.UserForm()
    return render(request, "login/login.html", locals())


def register(request):
    if request.session.get("is_login", None):
        return redirect("/index/")  # 不允许重复登录

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            password1 = register_form.cleaned_data.get("password1")
            password2 = register_form.cleaned_data.get("password2")
            if password1 != password2:
                message = "两次输入的密码不相同!"
                return render(request, "login/register.html", locals())

            username = register_form.cleaned_data.get("username")
            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:
                message = "用户名已经存在"
                return render(request, "login/register.html", locals())

            email = register_form.cleaned_data.get("email")
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:
                message = "该邮箱已经被注册了！"
                return render(request, "login/register.html", locals())

            new_user = models.User()
            new_user.name = username
            new_user.password = _hash_code(password1)
            new_user.email = email
            new_user.sex = register_form.cleaned_data.get("sex")
            new_user.save()
            return redirect("/login/")

        return render(request, "login/register.html", locals())

    register_form = forms.RegisterForm()
    return render(request, "login/register.html", locals())


def logout(request):
    if request.session.get("is_login", None):
        request.session.flush()
        return redirect("/login/")
    return redirect("/login/")
