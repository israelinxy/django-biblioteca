from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages  # Importar el sistema de mensajes de Django
from .models import Libro, Categoria  # Importar el modelo Libro y Categoria
from .forms import LibroForm  # Importar el formulario para crear/editar libros
from django.db.models import Q
from django.http import JsonResponse


# Verifica si el usuario es admin
def is_admin(user):
    return user.is_superuser


@login_required
# Vista para listar libros
def libro_list(request):
    query = request.GET.get(
        "q"
    )  # Capturamos el término de búsqueda desde el cuadro de búsqueda
    libros = Libro.objects.all()

    if query:
        libros = libros.filter(
            Q(titulo__icontains=query)  # Búsqueda por título
            | Q(autor__nombre__icontains=query)  # Búsqueda por nombre de autor
            | Q(autor__apellido__icontains=query)  # Búsqueda por apellido de autor
            | Q(editorial__nombre__icontains=query)  # Búsqueda por editorial
        )

    categorias = Categoria.objects.all()  # Obtener las categorías para los filtros
    return render(
        request,
        "gestion_libros/libros/libro_list.html",
        {"libros": libros, "categorias": categorias},
    )


# Vista para crear un nuevo libro
@user_passes_test(is_admin)
def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo libro
            messages.success(
                request, "El libro se ha creado con éxito."
            )  # Mensaje de éxito
            return redirect(
                "gestion_libros:libro_list"
            )  # Redirigir a la lista de libros
    else:
        form = LibroForm()
    return render(request, "gestion_libros/libros/libro_form.html", {"form": form})


# Vista para editar un libro existente
@user_passes_test(is_admin)
def libro_edit(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  # Obtener el libro por su ID
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()  # Guardar los cambios
            messages.success(
                request, "El libro se ha actualizado con éxito."
            )  # Mensaje de éxito
            return redirect(
                "gestion_libros:libro_list"
            )  # Redirigir a la lista de libros
    else:
        form = LibroForm(instance=libro)
    return render(request, "gestion_libros/libros/libro_form.html", {"form": form})


# Vista para eliminar un libro
@user_passes_test(is_admin)
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  # Obtener el libro por su ID
    if request.method == "POST":
        libro.delete()  # Eliminar el libro
        messages.success(
            request, "El libro se ha eliminado con éxito."
        )  # Mensaje de éxito
        return redirect("gestion_libros:libro_list")  # Redirigir a la lista de libros
    return render(
        request, "gestion_libros/libros/libro_confirm_delete.html", {"libro": libro}
    )


# Vista para confirmar la eliminación de un libro
@login_required
def libro_confirm_delete(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(
        request, "gestion_libros/libros/libro_confirm_delete.html", {"libro": libro}
    )


# Vista para autocompletado
def autocomplete_libros(request):
    if "term" in request.GET:
        query = request.GET.get("term")
        libros = Libro.objects.filter(
            Q(titulo__icontains=query)
            | Q(autor__nombre__icontains=query)
            | Q(autor__apellido__icontains=query)
            | Q(editorial__nombre__icontains=query)
        )
        suggestions = list(libros.values_list("titulo", flat=True))
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)
