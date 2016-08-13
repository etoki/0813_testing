#coding: utf8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label=u'username', max_length=64)
    password = forms.CharField(label=u'password', widget=forms.PasswordInput)

    def clean(self):
        if not self.cleaned_data.get('username') or not self.cleaned_data.get('password'):
            return None

        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        print ("#", user)
        if not user:
            raise forms.ValidationError('ユーザ名かパスワードが誤っています')
        self.cleaned_data['user'] = user
        return self.cleaned_data


class SignupForm(forms.Form):
    username = forms.CharField(label=u'username', max_length=64)
    password = forms.CharField(label=u'password', widget=forms.PasswordInput)

    def clean_username(self):
        if not self.cleaned_data.get('username'):
            return None
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('既にそのアドレスでユーザが登録されています')
        return self.cleaned_data['username']
