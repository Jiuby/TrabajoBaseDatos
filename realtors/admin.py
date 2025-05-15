from django.contrib import admin
from .models import Dueño

class DueñoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'fecha_inicio')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre', 'correo')
    list_per_page = 25
    readonly_fields = ('fecha_inicio',)

    def save_model(self, request, obj, form, change):
        # Solo encripta si es un nuevo dueño
        if not change:
            raw_password = form.cleaned_data.get('password')
            obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

admin.site.register(Dueño, DueñoAdmin)
