from django.db import models
from django.contrib.auth.models import User

# Lista de modelos creados


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey("Autor", on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    fecha_publicacion = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    editorial = models.ForeignKey(
        "Editorial",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    año_compra = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    libro = models.ForeignKey("Libro", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} por {self.usuario.username}"


class Reserva(models.Model):
    libro = models.ForeignKey("Libro", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.libro.titulo} por {self.usuario.username}"
