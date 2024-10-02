from django.urls import path
from . import views  # Importar las vistas de la app

app_name = "users"  # Namespace para la app users


# Definición de las rutas de la app `users`
urlpatterns = [
    path("login/", views.login_view, name="login"),  # Ruta para iniciar sesión
    path("register/", views.register_view, name="register"),  # Ruta para registrarse
    path(
        "profile/", views.profile_view, name="profile"
    ),  # Ruta para ver el perfil del usuario
    path("logout/", views.logout_view, name="logout"),  # Ruta para cerrar sesión
]
