# Importaciones necesarias
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language  # Importar la vista set_language

# Definición de las rutas principales del proyecto
urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta del panel de administración de Django
]

# Agrega las rutas de las aplicaciones con soporte para i18n
urlpatterns += i18n_patterns(
    # Rutas para las páginas estáticas
    path("", include("pages.urls")),  
    # Rutas de gestión de libros
    path("libros/", include("gestion_libros.urls")),  
    # Rutas de autenticación de usuarios
    path("usuarios/", include("users.urls")),  
    # Rutas de notificaciones
    path("notificaciones/", include("notifications.urls")),  
    # Esto permite acceder a la interfaz de traducción.
    path("rosetta/", include("rosetta.urls")),
)

# Agregar la ruta para cambiar el idioma
urlpatterns += [
    path('set_language/', set_language, name='set_language'),  # Esta ruta debe estar fuera de i18n_patterns
]
