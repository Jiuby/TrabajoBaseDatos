from django.contrib import admin

from .models import Contactos

class ContactosAdmin(admin.ModelAdmin):
    list_display=('id','nombre','propiedad','correo','fecha_contacto')
    list_display_link=('id','nombre')
    search_fields=('nombre','correo','propiedad')
    list_per_page=25
admin.site.register(Contactos, ContactosAdmin)

# Register your models here.
