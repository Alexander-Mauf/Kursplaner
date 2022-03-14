from django.contrib import admin
from . import models
from django.contrib.admin import register
# Register your models here.

@register(models.Kurs)
class KursAdmin(admin.ModelAdmin):
    pass

@register(models.Tagesplan)
class VerfuegbarkeitAdmin(admin.ModelAdmin):
    pass