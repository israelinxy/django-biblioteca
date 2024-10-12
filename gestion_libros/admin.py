from django.contrib import admin
from .models import Libro, Autor, Categoria, Editorial, Prestamo, Reserva
from django.utils.translation import gettext as _  # Importar gettext para traducción

# Models
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        _("titulo"),             
        _("autor"),              
        _("categoria"),          
        _("fecha_publicacion"),
        _("editorial"),          
        _("isbn"),               
        _("año_compra"),      
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
    list_display = (
        _("nombre"),             
        _("apellido"),   
    )
    search_fields = ("nombre", "apellido")
    ordering = ("apellido", "nombre")

    def total_libros(self, obj):
        return obj.libro_set.count()

    total_libros.short_description = _("Número de Libros")  


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (_("nombre"),)  
    search_fields = ("nombre",)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = (_("nombre"),)  
    search_fields = ("nombre",)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        _("libro"),               
        _("usuario"),             
        _("fecha_prestamo"),   
        _("fecha_devolucion"),  
    )
    list_filter = ("fecha_prestamo", "fecha_devolucion")
    search_fields = ("libro__titulo", "usuario__username")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        _("libro"),               
        _("usuario"),             
        _("fecha_reserva"),     
    )
    list_filter = ("fecha_reserva",)
    search_fields = ("libro__titulo", "usuario__username")
