from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Apellido"}
        ),
    )
    email = forms.EmailField(
        required=True,
        help_text="",  # Elimina el texto de ayuda predeterminado
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Correo Electrónico"}
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
                attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Contraseña"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Confirmar contraseña"}
            ),
        }
        labels = {
            "username": "Usuario",
            "password1": "Contraseña",
            "password2": "Confirmar Contraseña",
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina los textos de ayuda de todos los campos
        for field in self.fields.values():
            field.help_text = ""
