from django.contrib import admin
from .models import Libro, Autor, Categoria, Editorial, Prestamo, Reserva


# Models
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "categoria",
        "fecha_publicacion",
        "editorial",
        "isbn",
        "año_compra",
    )
    search_fields = (
        "titulo",
        "autor__nombre",
        "autor__apellido",
        "categoria__nombre",
        "editorial__nombre",
    )
    list_filter = ("categoria", "editorial", "fecha_publicacion")
    ordering = ("titulo", "fecha_publicacion")
    autocomplete_fields = ("autor", "categoria", "editorial")


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "total_libros")
    search_fields = ("nombre", "apellido")
    ordering = ("apellido", "nombre")

    def total_libros(self, obj):
        return obj.libro_set.count()

    total_libros.short_description = "Número de Libros"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "usuario", "fecha_prestamo", "fecha_devolucion")
    list_filter = ("fecha_prestamo", "fecha_devolucion")
    search_fields = ("libro__titulo", "usuario__username")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("libro", "usuario", "fecha_reserva")
    list_filter = ("fecha_reserva",)
    search_fields = ("libro__titulo", "usuario__username")
