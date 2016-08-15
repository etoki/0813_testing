from django.db import models


class Item(models.Model):
    test = models.CharField(max_length=64)
