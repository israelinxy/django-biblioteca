from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _  # Importar gettext para traducción


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Nombre")}  
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Apellido")}  
        ),
    )
    email = forms.EmailField(
        required=True,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": _("Correo Electrónico")}  
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        # Personalización de los widgets para los campos
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": _("Nombre de usuario")}  
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": _("Contraseña")}  
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": _("Confirmar contraseña")}  
            ),
        }
        labels = {
            "username": _("Usuario"),  
            "password1": _("Contraseña"),  
            "password2": _("Confirmar Contraseña"),  
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("Este correo ya está registrado."))  
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina los textos de ayuda de todos los campos
        for field in self.fields.values():
            field.help_text = ""
