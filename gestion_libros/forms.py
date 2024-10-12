from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _  # Importamos gettext_lazy para las traducciones
from .models import Libro, Autor, Categoria, Editorial


class LibroForm(forms.ModelForm):
    nuevo_autor = forms.CharField(
        required=False,
        max_length=100,
        label=_("Nuevo Autor"),
        help_text=_("Añade un nuevo autor si no está en la lista."), 
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    nueva_categoria = forms.CharField(
        required=False,
        max_length=100,
        label=_("Nueva Categoría"), 
        help_text=_("Añade una nueva categoría si no está en la lista."), 
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    nueva_editorial = forms.CharField(
        required=False,
        max_length=100,
        label=_("Nueva Editorial"), 
        help_text=_("Añade una nueva editorial si no está en la lista."), 
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    fecha_publicacion = forms.IntegerField(
        required=False,
        label=_("Año de Publicación"), 
        help_text=_("Introduce solo el año de publicación."), 
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": _("Ej: 2024")} 
        ),
        min_value=1000,
        max_value=9999,
    )
    isbn = forms.CharField(
        required=False,
        label=_("ISBN"), 
        help_text=_("Introduce el ISBN del libro (13 caracteres)."), 
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=13,
    )
    editorial = forms.ModelChoiceField(
        queryset=Editorial.objects.all(),
        required=False,
        label=_("Editorial"), 
        help_text=_("Selecciona una editorial o añade una nueva."), 
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    año_compra = forms.IntegerField(
        required=False,
        label=_("Año de Compra"), 
        help_text=_("Introduce el año en que la biblioteca compró este libro."), 
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": _("Ej: 2023")}), 
        min_value=1900,
        max_value=timezone.now().year,  # Hasta el año actual
    )

    class Meta:
        model = Libro
        fields = [
            "titulo",
            "autor",
            "categoria",
            "fecha_publicacion",
            "isbn",
            "editorial",
            "año_compra",
        ]
        widgets = {
            "autor": forms.Select(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        self.fields["autor"].required = False
        self.fields["categoria"].required = False

    def clean(self):
        cleaned_data = super().clean()
        autor = cleaned_data.get("autor")
        nuevo_autor = cleaned_data.get("nuevo_autor")
        categoria = cleaned_data.get("categoria")
        nueva_categoria = cleaned_data.get("nueva_categoria")
        editorial = cleaned_data.get("editorial")
        nueva_editorial = cleaned_data.get("nueva_editorial")

        # Validación: al menos un campo de autor debe estar lleno
        if not autor and not nuevo_autor:
            raise forms.ValidationError(
                _("Debes seleccionar un autor o añadir uno nuevo.") 
            )

        # Validación: al menos un campo de categoría debe estar lleno
        if not categoria and not nueva_categoria:
            raise forms.ValidationError(
                _("Debes seleccionar una categoría o añadir una nueva.") 
            )

        # Validación: al menos un campo de editorial debe estar lleno
        if not editorial and not nueva_editorial:
            raise forms.ValidationError(
                _("Debes seleccionar una editorial o añadir una nueva.") 
            )

        return cleaned_data

    def save(self, commit=True):
        # Lógica para crear un nuevo autor si se ha ingresado uno
        nuevo_autor = self.cleaned_data.get("nuevo_autor")
        if nuevo_autor:
            autor_obj, created = Autor.objects.get_or_create(nombre=nuevo_autor)
            self.instance.autor = autor_obj

        # Lógica para crear una nueva categoría si se ha ingresado una
        nueva_categoria = self.cleaned_data.get("nueva_categoria")
        if nueva_categoria:
            categoria_obj, created = Categoria.objects.get_or_create(
                nombre=nueva_categoria
            )
            self.instance.categoria = categoria_obj

        # Lógica para crear una nueva editorial si se ha ingresado una
        nueva_editorial = self.cleaned_data.get("nueva_editorial")
        if nueva_editorial:
            editorial_obj, created = Editorial.objects.get_or_create(
                nombre=nueva_editorial
            )
            self.instance.editorial = editorial_obj

        return super().save(commit=commit)
