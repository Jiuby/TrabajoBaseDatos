from django.db import models
from datetime import datetime
from realtors.models import Dueño


DEPARTAMENTOS_CHOICES = [
    ('AMA', 'Amazonas'),
    ('ANT', 'Antioquia'),
    ('ARA', 'Arauca'),
    ('ATL', 'Atlántico'),
    ('BOL', 'Bolívar'),
    ('BOY', 'Boyacá'),
    ('CAL', 'Caldas'),
    ('CAQ', 'Caquetá'),
    ('CAS', 'Casanare'),
    ('CAU', 'Cauca'),
    ('CES', 'Cesar'),
    ('CHO', 'Chocó'),
    ('COR', 'Córdoba'),
    ('CUN', 'Cundinamarca'),
    ('DC',  'Bogotá, D.C.'),
    ('GUA', 'Guainía'),
    ('GUV', 'Guaviare'),
    ('HUI', 'Huila'),
    ('LAG', 'La Guajira'),
    ('MAG', 'Magdalena'),
    ('MET', 'Meta'),
    ('NAR', 'Nariño'),
    ('NSA', 'Norte de Santander'),
    ('PUT', 'Putumayo'),
    ('QUI', 'Quindío'),
    ('RIS', 'Risaralda'),
    ('SAN', 'Santander'),
    ('SAP', 'San Andrés y Providencia'),
    ('SUC', 'Sucre'),
    ('TOL', 'Tolima'),
    ('VAC', 'Valle del Cauca'),
    ('VAU', 'Vaupés'),
    ('VID', 'Vichada'),
]
# Create your models here.

class Propiedad(models.Model):
    dueño = models.ForeignKey(Dueño, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=3, choices=DEPARTAMENTOS_CHOICES)
    codigoPostal = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    habitaciones = models.IntegerField()
    baños = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    tamaño = models.IntegerField()
    tamaño_lote = models.DecimalField(max_digits=5, decimal_places=1)
    foto_principal = models.ImageField(upload_to='photos/%Y/%m/%d')
    foto_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    esta_publicado = models.BooleanField(default=True)
    lista_dato = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo
