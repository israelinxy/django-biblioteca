from django.urls import path
from .views import LoginView, RegisterView, ProfileView, LogoutView  # Importar las vistas de la app

app_name = "users"  # Namespace para la app users

# Definición de las rutas de la app `users`
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),  # Ruta para iniciar sesión
    path("register/", RegisterView.as_view(), name="register"),  # Ruta para registrarse
    path("profile/", ProfileView.as_view(), name="profile"),  # Ruta para ver el perfil del usuario
    path("logout/", LogoutView.as_view(), name="logout"),  # Ruta para cerrar sesión
]
