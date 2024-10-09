from django.urls import path
from .views import HomeView, AboutView, ContactView

app_name = "pages"  # Namespace para la app pages

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # Ruta para la página de inicio
    path("sobre/", AboutView.as_view(), name="about"),  # Ruta para la página "Sobre nosotros"
    path("contacto/", ContactView.as_view(), name="contact"),  # Ruta para la página de contacto
]
