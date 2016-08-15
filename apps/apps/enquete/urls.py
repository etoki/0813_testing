# coding: utf-8
from django.conf.urls import url
from apps.enquete import views


urlpatterns = [
    url(r'^test$', views.test, name='test'),
]
