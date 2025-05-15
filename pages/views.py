from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Propiedad
from realtors.models import Dueño
from listings.choices import precios, habitaciones, departamentos



# Create your views here.
def index(request):
    propiedad = Propiedad.objects.order_by('-lista_dato').filter(esta_publicado=True)[:3]
    
    context ={
        'listings': propiedad,
        'state_choices':departamentos,
        'bedroom_choices':habitaciones,
        'price_choices':precios,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors=Dueño.objects.order_by('-fecha_inicio')

    mvp_realtors=Dueño.objects.all().filter(activo=True)

    context= {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }


    return render(request, 'pages/about.html', context)
