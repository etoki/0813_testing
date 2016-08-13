#coding: utf8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import (
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

from apps.account.forms import (
    SignupForm,
    LoginForm,
)


def signup(request):
    if request.method == 'GET':
        return render(request, "account/signup.html", {
            'form': SignupForm()
        })
    form = SignupForm(request.POST)
    if not form.is_valid():
        return render(request, "account/signup.html", {
            'form': form,
        })

    test = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    # ユーザの作成 & ログイン
    user = User.objects.create(username=form.cleaned_data['username'])
    user.set_password(form.cleaned_data['password'])
    user.save()
    # http://docs.djangoproject.jp/en/latest/topics/auth.html
    if request.method == 'GET':
        return render(request, "account/signup.html", {
            'form': LoginForm()
        })
    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, "account/signup.html", {
            'form': form,
        })
    auth_login(request, form.cleaned_data['user'])
    return HttpResponseRedirect(reverse('account:mypage'))


@login_required  # ログイン必須のview
def mypage(request):
    return render(request, "account/mypage.html", {
    })


def login(request):
    if request.method == 'GET':
        return render(request, "account/login.html", {
            'form': LoginForm()
        })
    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, "account/login.html", {
            'form': form,
        })
    auth_login(request, form.cleaned_data['user'])
    return HttpResponseRedirect(reverse('account:mypage'))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('account:login'))
