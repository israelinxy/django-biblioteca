from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Vista para iniciar sesión
def login_view(request):
    # Verificar si hay un usuario autenticado
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Mostrar mensaje si el usuario autenticado es un superusuario
            messages.warning(
                request,
                "Ya estás autenticado como superusuario. Cierra sesión antes de iniciar con otra cuenta.",
            )
        else:
            # Mostrar mensaje si el usuario autenticado es un usuario normal
            messages.warning(
                request,
                "Ya hay un usuario autenticado. Cierra sesión primero para iniciar con otra cuenta.",
            )
        return redirect("users:profile")  # Redirigir al perfil del usuario autenticado

    # Procesar la solicitud de inicio de sesión
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("users:profile")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# Vista para registrarse
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "¡Registro exitoso! Has iniciado sesión automáticamente."
            )
            login(request, user)

            return redirect("users:profile")
        else:
            messages.error(request, "Por favor, corrige los errores a continuación.")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


# Vista para ver el perfil del usuario
@login_required  # Requiere que el usuario esté autenticado
def profile_view(request):
    return render(request, "users/profile.html", {"user": request.user})


# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # Cerrar sesión
    messages.success(request, "Has cerrado sesión con éxito.")
    return redirect("pages:home")  # Redirigir a la página de inicio
