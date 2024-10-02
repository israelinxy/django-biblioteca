from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages


# Vista para la página de inicio
def home(request):
    return render(request, "pages/home.html")


# Vista para la página "Sobre nosotros"
def about(request):
    return render(request, "pages/about.html")


# Vista para la página de contacto
def contact(request):
    if request.method == "POST":
        message = request.POST.get("message")

        if not message:
            # Mensaje de error si el campo está vacío
            messages.error(request, "Por favor, escribe un mensaje antes de enviar.")
            return redirect("pages:contact")
        try:
            # Envía el correo electrónico
            send_mail(
                subject="Nuevo mensaje de contacto",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            # Mensaje de éxito
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("pages:contact")
        except BadHeaderError:
            # Mensaje de error específico si ocurre un problema con la cabecera
            messages.error(
                request, "Se ha producido un error con la cabecera del correo."
            )
            return redirect("contact")
        except Exception as e:
            # Mensaje genérico de error para cualquier otra excepción
            messages.error(request, f"Error al enviar el mensaje: {str(e)}")
            return redirect("contact")

    return render(request, "pages/contact.html")


# Vista para la página de preguntas frecuentes
def faq(request):
    return render(request, "pages/faq.html")
