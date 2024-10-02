from django.urls import path
from . import views  # Importar las vistas de la app
from .views import home, about, contact, faq

app_name = "pages"  # Definición del namespace

# Definición de las rutas de la app `pages`
urlpatterns = [
    path("", views.home, name="home"),  # Ruta para la página de inicio
    path("about/", views.about, name="about"),  # Ruta para la página "Sobre nosotros"
    path("contact/", views.contact, name="contact"),  # Ruta para la página de contacto
]
