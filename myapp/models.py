from django.db import models

# Create your models here.
class Alimodel(models.Model):
    name = models.CharField(max_length=50)
