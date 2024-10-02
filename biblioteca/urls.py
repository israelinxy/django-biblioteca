# Importaciones necesarias
from django.contrib import admin
from django.urls import path, include

# Definicion de las rutas principales del proyecto
urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta del panel de administración de Django
    path("", include("pages.urls")),  # Rutas para las páginas estáticas
    path("libros/", include("gestion_libros.urls")),  # Rutas de gestión de libros
    path("usuarios/", include("users.urls")),  # Rutas de autenticación de usuarios
    path("notificaciones/", include("notifications.urls")),  # Rutas de notificaciones
]
