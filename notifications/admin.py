from django.contrib import admin
from .models import Notification
from django.utils.translation import gettext as _  # Importar gettext para traducción

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        _("titulo"),          
        _("usuario"),         
        _("fecha_creacion"),
        _("leido")            
    )
    search_fields = ("titulo",)
    list_filter = ("leido",)
