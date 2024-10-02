from django.urls import path
from . import views

app_name = "notifications"  # Definición del namespace

urlpatterns = [
    path(
        "", views.notification_list, name="notification_list"
    ),  # Listar notificaciones
    path(
        "<int:pk>/", views.notification_detail, name="notification_detail"
    ),  # Detalle de notificación
]
