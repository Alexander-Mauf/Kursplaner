from django.contrib import admin
from django.contrib.admin import register

from . import models


@register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "timeslot",
        "teacher",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    filter_horizontal = ('students',)
    list_filter = ("teacher",)
    search_fields = ("=hash_id", "=pp_user_id")


@register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "can_ski_alpin",
        "can_snowboard",
        "has_licence"
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    list_filter = ("can_ski_alpin", "can_snowboard", "can_ski_telemark", "can_ski_cross_country")
    search_fields = ("name", "surname")


@register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "surname")


@register(models.Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "teacher",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    search_fields = ("teacher__name",)


@register(models.Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
