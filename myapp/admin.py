from django.contrib import admin

# Register your models here.
from .models import Alimodel

@admin.register(Alimodel)
class AlimodelAdmin(admin.ModelAdmin):
    list_display = ['name']