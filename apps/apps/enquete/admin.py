# coding: utf-8
from django.contrib import admin
from models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'test',)
    list_display_links = ('id', 'test',)
admin.site.register(Item, ItemAdmin)
