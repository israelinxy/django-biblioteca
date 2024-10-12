from django.shortcuts import render, redirect  # Importar render y redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.utils.translation import gettext as _  # Importar gettext para traducción


# Vista para iniciar sesión
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')  # Solo devuelve la plantilla sin formulario

    def post(self, request):
        # Captura los datos de usuario y contraseña directamente desde el POST
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("Has iniciado sesión con éxito."))  
            return redirect('users:profile')
        else:
            messages.error(request, _("Nombre de usuario o contraseña incorrectos."))  

        return render(request, 'users/login.html')  # Vuelve a renderizar la plantilla en caso de error


# Vista para registrarse
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Registro exitoso. Ya puedes iniciar sesión."))  
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})


# Vista para ver el perfil del usuario
class ProfileView(View):
    def get(self, request):
        return render(request, 'users/profile.html')


# Vista para cerrar sesión
class LogoutView(DjangoLogoutView):
    def get(self, request, *args, **kwargs):
        messages.success(request, _("Has cerrado sesión con éxito."))  
        return super().get(request, *args, **kwargs)
