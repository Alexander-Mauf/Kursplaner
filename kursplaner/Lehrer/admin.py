from django.contrib import admin
from . import models
from django.contrib.admin import register

# Register your models here.

@register(models.Lehrer)
class LehrerAdmin(admin.ModelAdmin):
    def _period_of_validity(self, obj):
        min_date = None
        max_date = None
        for door in obj.doors.all():
            if min_date == None or door.starts_at < min_date:
                min_date = door.starts_at
            if max_date == None or door.ends_at > max_date:
                max_date = door.ends_at
        # return f"{min_date} - {max_date}"
        return render_to_string("calendar_core/admin/showtime_period.html", context={
                "min_date": min_date,
                "max_date": max_date
            })

    _period_of_validity.short_description = ("Laufzeit")
    pass

