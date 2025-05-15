from django.contrib import admin

# Register your models here.

from .models import Propiedad


class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'esta_publicado',
                    'precio', 'lista_dato', 'dueño')
    list_display_links = ('id', 'titulo')
    list_filter = ('dueño',)
    list_editable = ('esta_publicado',)
    search_fields = ('titulo', 'descripcion', 'direccion',
                     'ciudad', 'departamento', 'codigoPostal', 'precio')
    list_per_page = 25


admin.site.register(Propiedad, PropiedadAdmin)
