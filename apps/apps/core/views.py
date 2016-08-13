#coding: utf8
from django.http import (
    HttpResponse
)
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {
    })


def http404(request):
    """ 404 ページ """
    return HttpResponse("ページが見つかりません")


def http500(request):
    """ 500 ページ """
    return HttpResponse("Server Error")
