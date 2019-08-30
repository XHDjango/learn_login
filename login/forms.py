# -*- coding: utf-8 -*-
"""
@Author: xiaohao
@Date: 2019/8/30
"""

from django import forms
from captcha.fields import CaptchaField

USERNAME_ATTRS = {'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}
PASSWORD_ATTRS = {'class': 'form-control', 'placeholder': "Password"}


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs=USERNAME_ATTRS))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs=PASSWORD_ATTRS))
    captcha = CaptchaField(label="验证码")


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs=USERNAME_ATTRS))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs=PASSWORD_ATTRS))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs=PASSWORD_ATTRS))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
