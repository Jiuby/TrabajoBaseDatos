from django.db import models
from datetime import datetime
# Create your models here.

class Contactos(models.Model):
    propiedad=models.CharField(max_length=200)
    propiedad_id=models.IntegerField()
    nombre=models.CharField(max_length=200)
    correo=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    mensaje=models.TextField(blank=True)
    fecha_contacto=models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True)
    def __str__(self):
        return self.nombre