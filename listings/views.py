from django.shortcuts import get_object_or_404, render
from .models import Propiedad
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import precios, habitaciones, departamentos


# Create your views here.


def index(request):
    listings = Propiedad.objects.order_by('-lista_dato').filter(esta_publicado=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def lisitng(request, listing_id):
    listing=get_object_or_404(Propiedad, pk=listing_id)

    context = {
        'listing': listing  # ✅ Aquí va la instancia, no la clase
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list=Propiedad.objects.order_by('-lista_dato')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
        
   #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(ciudad__iexact = city)

     #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list=queryset_list.filter(departamento__iexact = state)
    
    
     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(habitaciones__lte=bedrooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(precio__lte=price)
                
    context={
        'state_choices':departamentos,
        'bedroom_choices':habitaciones,
        'price_choices':precios,
        'listings':queryset_list,
        'values':request.GET,
    }

    return render(request, 'listings/search.html', context)
