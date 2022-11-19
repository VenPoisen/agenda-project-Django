from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)


class Contact(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    criation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
