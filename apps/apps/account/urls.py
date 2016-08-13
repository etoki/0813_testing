# coding: utf-8
from django.conf.urls import url
from apps.account import views

urlpatterns = [
    url(r'^signup$', views.signup, name="signup"),
    url(r'^mypage$', views.mypage, name="mypage"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
]
