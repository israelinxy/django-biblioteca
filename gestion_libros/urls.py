from django.urls import path
from . import views  # Importar las vistas de la app
from .views import (
    libro_list,
    libro_create,
    libro_edit,
    libro_delete,
    libro_confirm_delete,
)


app_name = "gestion_libros"  # Namespace para la app gestion_libros


# Definición de las rutas de la app `gestion_libros`
urlpatterns = [
    path("", views.libro_list, name="libro_list"),  # Ruta para listar libros
    path(
        "crear/", views.libro_create, name="libro_create"
    ),  # Ruta para crear un nuevo libro
    path(
        "editar/<int:pk>/", views.libro_edit, name="libro_edit"
    ),  # Ruta para editar un libro
    path(
        "eliminar/<int:pk>/", views.libro_delete, name="libro_delete"
    ),  # Ruta para eliminar un libro
    path(
        "confirmar_eliminar/<int:id>/",
        views.libro_confirm_delete,
        name="libro_confirm_delete",
    ),  # Ruta para confirmar la eliminacion de un libro
]
