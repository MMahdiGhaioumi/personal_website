from django.contrib import admin
from django.utils.html import format_html
from unfold import admin as unfold_admin
from . import models


@admin.register(models.Service)
class ServiceAdmin(unfold_admin.ModelAdmin):
    list_display = ('__str__', 'show_image')

    @admin.display(description="نگاره سروس")
    def show_image(self, obj):
        return format_html(
            f'<div style="background: black; width: 200px; height: 80px; justify-content: center; align-items: center; display: flex;"><img src="{obj.icon.url}" width="300pxpx" height="80px"></div>')


@admin.register(models.Resume)
class ResumeAdmin(unfold_admin.ModelAdmin):
    radio_fields = {'place': admin.HORIZONTAL}


admin.site.register(models.Skill)
