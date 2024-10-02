from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "fecha_creacion", "leido")
    search_fields = ("titulo",)
    list_filter = ("leido",)
