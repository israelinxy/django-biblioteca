from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django import forms

# Formulario para el contacto
class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)

# Vista para la página de inicio
class HomeView(TemplateView):
    template_name = "pages/home.html"  # El template asociado

# Vista para la página "Sobre nosotros"
class AboutView(TemplateView):
    template_name = "pages/about.html"  # El template asociado

# Vista para la página de contacto
class ContactView(FormView):
    template_name = "pages/contact.html"  # El template asociado
    form_class = ContactForm  # El formulario a usar

    def form_valid(self, form):
        """
        Este método se llama si el formulario es válido.
        Envía el correo electrónico y muestra un mensaje de éxito.
        """
        message = form.cleaned_data['message']
        try:
            send_mail(
                subject="Nuevo mensaje de contacto",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(self.request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("pages:contact")
        except BadHeaderError:
            messages.error(self.request, "Se ha producido un error con la cabecera del correo.")
            return redirect("pages:contact")
        except Exception as e:
            messages.error(self.request, f"Error al enviar el mensaje: {str(e)}")
            return redirect("pages:contact")

    def form_invalid(self, form):
        """
        Este método se llama si el formulario no es válido.
        Muestra un mensaje de error.
        """
        messages.error(self.request, "Por favor, escribe un mensaje antes de enviar.")
        return super().form_invalid(form)
