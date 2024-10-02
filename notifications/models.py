from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Modelo para notificaciones


class Notification(models.Model):
    titulo = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
