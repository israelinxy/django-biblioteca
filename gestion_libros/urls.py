from django.urls import path
from .views import (
    LibroListView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
    LibroEstadisticsView,
)

app_name = "gestion_libros"  # Namespace para la app gestion_libros

# Definición de las rutas de la app `gestion_libros`
urlpatterns = [
    path("", LibroListView.as_view(), name="libro_list"),  # Ruta para listar libros
    path("crear/", LibroCreateView.as_view(), name="libro_create"),  # Ruta para crear un nuevo libro
    path("editar/<int:pk>/", LibroUpdateView.as_view(), name="libro_edit"),  # Ruta para editar un libro
    path("eliminar/<int:pk>/", LibroDeleteView.as_view(), name="libro_delete"),  # Ruta para eliminar un libro
    path("confirmar_eliminar/<int:pk>/", LibroDeleteView.as_view(), name="libro_confirm_delete"),  # Ruta para confirmar la eliminación de un libro
    path("estadisticas/", LibroEstadisticsView.as_view(), name="libro_estadistics"),  # Ruta para ver las estadísticas de los libros
]
