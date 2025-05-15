from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

class Dueño(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='photo/%Y/%m/%d')
    descripcion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=128)  # Contraseña encriptada
    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre

    def set_password(self, raw_password):
        """Encripta la contraseña antes de guardarla"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica si una contraseña sin encriptar coincide con la guardada"""
        return check_password(raw_password, self.password)
