from django.urls import path
from .views import NotificationListView, NotificationDetailView

app_name = "notifications"  # Namespace para la app notifications

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification_list"),  # Ruta para listar notificaciones
    path("<int:notification_id>/", NotificationDetailView.as_view(), name="notification_detail"),  # Ruta para detalle de una notificación
]
