from django.db import models
from django.forms import CharField

# Create your models here.


class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    releseDate=models.DateField()
    desc=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
