from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages  # Importar el sistema de mensajes de Django
from .models import Libro, Categoria  # Importar el modelo Libro y Categoria
from .forms import LibroForm  # Importar el formulario para crear/editar libros
from django.db.models import Count, Q
from django.urls import reverse_lazy


# Verifica si el usuario es admin
class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class LibroListView(LoginRequiredMixin, ListView):
    model = Libro  # El modelo que queremos listar
    template_name = "gestion_libros/libros/libro_list.html"  # El template asociado
    context_object_name = "libros"  # Cómo llamamos la lista de libros en el template
    ordering = ["titulo"]  # Ordenación por defecto
    paginate_by = 3  # Paginar los resultados

    def get_queryset(self):
        """
        Personaliza el queryset para filtrar y ordenar los libros según los parámetros.
        """
        query = self.request.GET.get("q")
        sort_by = self.request.GET.get("sort", "titulo")
        order = self.request.GET.get("order", "asc")
        categoria_id = self.request.GET.get("categoria")

        libros = Libro.objects.all()

        if query:
            libros = libros.filter(
                Q(titulo__icontains=query)
                | Q(autor__nombre__icontains=query)
                | Q(autor__apellido__icontains=query)
                | Q(editorial__nombre__icontains=query)
            )

        valid_sort_fields = {
            "titulo": "titulo",
            "fecha_publicacion": "fecha_publicacion",
            "editorial": "editorial__nombre",
            "categoria": "categoria__nombre",
        }

        sort_field = valid_sort_fields.get(sort_by, "titulo")

        if order == "desc":
            sort_field = f"-{sort_field}"

        libros = libros.order_by(sort_field)

        if categoria_id:
            libros = libros.filter(categoria__id=categoria_id)

        return libros

    def get_context_data(self, **kwargs):
        """
        Agregar más contexto al template como las categorías y los parámetros de búsqueda.
        """
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["query"] = self.request.GET.get("q")
        context["sort_by"] = self.request.GET.get("sort", "titulo")
        context["order"] = self.request.GET.get("order", "asc")
        context["categoria_seleccionada"] = self.request.GET.get("categoria")
        return context


# Vista para crear un nuevo libro
class LibroCreateView(LoginRequiredMixin, IsAdminMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "gestion_libros/libros/libro_form.html"
    success_url = reverse_lazy("gestion_libros:libro_list")  # Redirigir a la lista de libros después de crear

    def form_valid(self, form):
        messages.success(self.request, _("El libro se ha creado con éxito."))  # Mensaje de éxito
        return super().form_valid(form)


# Vista para editar un libro existente
class LibroUpdateView(LoginRequiredMixin, IsAdminMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "gestion_libros/libros/libro_form.html"
    success_url = reverse_lazy("gestion_libros:libro_list")  # Redirigir a la lista de libros después de actualizar

    def form_valid(self, form):
        messages.success(self.request, _("El libro se ha actualizado con éxito."))  # Mensaje de éxito
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(Libro, pk=self.kwargs['pk'])


# Vista para eliminar un libro
class LibroDeleteView(LoginRequiredMixin, IsAdminMixin, DeleteView):
    model = Libro
    template_name = "gestion_libros/libros/libro_confirm_delete.html"
    success_url = reverse_lazy("gestion_libros:libro_list")  # Redirigir a la lista de libros después de eliminar

    def form_valid(self, form):
        messages.success(self.request, _("El libro se ha eliminado con éxito."))  # Mensaje de éxito
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(Libro, pk=self.kwargs['pk'])


# Vista para ver las estadísticas de libros
class LibroEstadisticsView(LoginRequiredMixin, IsAdminMixin, TemplateView):
    template_name = 'gestion_libros/libros/libro_estadistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener estadísticas de libros por categoría
        libros_por_categoria = Categoria.objects.annotate(total_libros=Count('libro'))

        # Obtener estadísticas de libros por año de compra
        libros_por_año_compra = (
            Libro.objects.values('año_compra')
            .annotate(total_libros=Count('id'))
            .order_by('año_compra')
        )

        # Calcular el total de libros para superusuario
        total_libros = Libro.objects.count()

        context.update({
            'libros_por_categoria': libros_por_categoria,
            'libros_por_año_compra': libros_por_año_compra,
            'total_libros': total_libros,
        })

        return context
