from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Notification  # Asegúrate de tener un modelo Notification

# Vista para listar notificaciones
class NotificationListView(ListView):
    model = Notification  # El modelo que queremos listar
    template_name = "notifications/notification_list.html"  # El template asociado
    context_object_name = "notificaciones"  # Cómo llamamos la lista de notificaciones en el template

    def get_queryset(self):
        """
        Personaliza el queryset si es necesario.
        Aquí puedes agregar filtros o personalizaciones adicionales.
        """
        return Notification.objects.all()  # Obtener todas las notificaciones


# Vista para detalle de una notificación
class NotificationDetailView(DetailView):
    model = Notification  # El modelo para obtener la notificación
    template_name = "notifications/notification_detail.html"  # El template asociado
    context_object_name = "notificacion"  # Cómo llamamos la notificación en el template
    pk_url_kwarg = "notification_id"  # El nombre del argumento de la URL que contiene el ID

    def get_object(self):
        """
        Personaliza la obtención del objeto.
        """
        return get_object_or_404(Notification, id=self.kwargs["notification_id"])
