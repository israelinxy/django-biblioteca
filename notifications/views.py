from django.shortcuts import render, get_object_or_404
from .models import Notification  # Asegúrate de tener un modelo Notification


# Vista para listar notificaciones
def notification_list(request):
    notifications = Notification.objects.all()  # Obtener todas las notificaciones
    return render(
        request,
        "notifications/notification_list.html",
        {"notificaciones": notifications},
    )


# Vista para detalle de una notificación
def notification_detail(request, notification_id):
    notification = get_object_or_404(
        Notification, id=notification_id
    )  # Obtener la notificación específica
    return render(
        request,
        "notifications/notification_detail.html",
        {"notificacion": notification},
    )
