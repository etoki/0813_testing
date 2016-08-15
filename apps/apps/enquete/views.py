#coding: utf8
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from models import Item
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


def test(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return HttpResponseRedirect('test')
    else:
        form = ItemForm()
    return render_to_response('enquete/test.html',dict(form=form))
