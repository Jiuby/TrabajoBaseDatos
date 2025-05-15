from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contactos
from django.core.mail import send_mail

def Contactos(request):
    if request.method=='POST':
        propiedad_id=request.POST['listing_id']
        propiedad =request.POST['listing']
        nombre =request.POST['name']
        correo =request.POST['email']
        celular =request.POST['phone']
        mensaje =request.POST['message']
        user_id =request.POST['user_id']
        realtor_email =request.POST['realtor_email']

        # check if user has made inquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Contactos.objects.all().filter(listing_id=propiedad_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Ya has hecho una consulta sobre esta propiedad')
                return redirect('/listings/'+propiedad_id)

        contact=Contactos(listing=propiedad, listing_id=propiedad_id, name=nombre, email=correo,phone=celular, message=mensaje, user_id=user_id)

        contact.save()

        # Send mail

        # send_mail (
        #         'Property Listing Inquiry',
        #         'There has been an inquiry for' + listing + '.Sign into the admin panel for more info',
        #         'jcrocks34@gmail.com',
        #         [realtor_email,'krishultimate0010@gmail.com','manumanoj0010@gmail.com'],
        #         fail_silently=False

        # )
                
        



        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+propiedad_id)



