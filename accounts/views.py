from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contactos
from realtors.models import Dueño
from listings.models import  Propiedad, Dueño, DEPARTAMENTOS_CHOICES
from datetime import datetime

# Create your views here.
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match 
        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Ese usuario ya existe')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Ese email ya esta en uso')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    user.save()
                    messages.success(request,'Ya estas registrado, puedes iniciar sesion')
                    return redirect('login')

        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 1. Autenticación como User de Django
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Bienvenido, has iniciado sesión como usuario')
            return redirect('dashboard')  # Redirige al dashboard de usuarios

        # 2. Autenticación como Dueño (usando correo)
        try:
            dueño = Dueño.objects.get(correo=username)
            if dueño.check_password(password):
                # Guardar dueño en la sesión
                request.session['dueño_id'] = dueño.id
                messages.success(request, f'Bienvenido, {dueño.nombre} (Dueño)')
                return redirect('dashboard_dueno')
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Dueño.DoesNotExist:
            messages.error(request, 'Credenciales inválidas')

        return redirect('login')  # Si falló todo

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        # Cierra sesión si es un usuario autenticado de Django
        auth.logout(request)

        # Cierra sesión si es un dueño autenticado por sesión
        if 'dueño_id' in request.session:
            del request.session['dueño_id']

        messages.success(request, 'Acabas de salir de tu cuenta')
        return redirect('index')

def dashboard(request):
    user_contacts= Contactos.objects.order_by('-fecha_contacto').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)

def dashboard_dueno(request):
    dueño_id = request.session.get('dueño_id')
    if not dueño_id:
        return redirect('login_dueño')

    propiedades = Propiedad.objects.filter(dueño_id=dueño_id)

    return render(request, 'accounts/dashboard_admin.html', {'propiedades': propiedades})

def crear_propiedad(request):
    dueño_id = request.session.get('dueño_id')
    if not dueño_id:
        return redirect('login')

    if request.method == 'POST':
        dueño = Dueño.objects.get(id=dueño_id)

        nueva = Propiedad(
            dueño=dueño,
            titulo=request.POST['titulo'],
            direccion=request.POST['direccion'],
            ciudad=request.POST['ciudad'],
            departamento=request.POST['departamento'],
            codigoPostal=request.POST['codigoPostal'],
            descripcion=request.POST.get('descripcion', ''),
            precio=request.POST['precio'],
            habitaciones=request.POST['habitaciones'],
            baños=request.POST['baños'],
            garage=request.POST.get('garage', 0),
            tamaño=request.POST['tamaño'],
            tamaño_lote=request.POST['tamaño_lote'],
            foto_principal=request.FILES['foto_principal'],
            foto_1=request.FILES.get('foto_1'),
            foto_2=request.FILES.get('foto_2'),
            foto_3=request.FILES.get('foto_3'),
            foto_4=request.FILES.get('foto_4'),
            foto_5=request.FILES.get('foto_5'),
            foto_6=request.FILES.get('foto_6'),
            esta_publicado=True,
            lista_dato=datetime.now()
        )
        nueva.save()
        messages.success(request, 'Propiedad creada exitosamente.')
        return redirect('dashboard_dueno')

    context = {
        'departamentos': DEPARTAMENTOS_CHOICES
    }
    return render(request, 'listings/crear_propiedad.html', context)


def editar_propiedad(request, propiedad_id):
    dueño_id = request.session.get('dueño_id')
    if not dueño_id:
        return redirect('login')

    propiedad = get_object_or_404(Propiedad, id=propiedad_id, dueño_id=dueño_id)

    if request.method == 'POST':
        propiedad.titulo = request.POST['titulo']
        propiedad.direccion = request.POST['direccion']
        propiedad.ciudad = request.POST['ciudad']
        propiedad.departamento = request.POST['departamento']
        propiedad.codigoPostal = request.POST['codigoPostal']
        propiedad.descripcion = request.POST.get('descripcion', '')
        propiedad.precio = request.POST['precio']
        propiedad.habitaciones = request.POST['habitaciones']
        propiedad.baños = request.POST['baños']
        propiedad.garage = request.POST.get('garage', 0)
        propiedad.tamaño = request.POST['tamaño']
        propiedad.tamaño_lote = request.POST['tamaño_lote']

        # Si subieron nuevas fotos, reemplazarlas
        if 'foto_principal' in request.FILES:
            propiedad.foto_principal = request.FILES['foto_principal']
        for i in range(1, 7):
            key = f'foto_{i}'
            if key in request.FILES:
                setattr(propiedad, key, request.FILES[key])

        propiedad.save()
        messages.success(request, 'Propiedad actualizada correctamente.')
        return redirect('dashboard_dueno')

    context = {
        'propiedad': propiedad,
        'departamentos': DEPARTAMENTOS_CHOICES
    }
    return render(request, 'listings/editar_propiedad.html', context)

def eliminar_propiedad(request, propiedad_id):
    dueño_id = request.session.get('dueño_id')
    if not dueño_id:
        return redirect('login')

    propiedad = get_object_or_404(Propiedad, id=propiedad_id, dueño_id=dueño_id)

    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, 'Propiedad eliminada correctamente.')
        return redirect('dashboard_dueno')

    return render(request, 'listings/confirmar_eliminacion.html', {'propiedad': propiedad})

def publicar_propiedad(request, propiedad_id):
    dueño_id = request.session.get('dueño_id')
    if not dueño_id:
        return redirect('login')

    propiedad = get_object_or_404(Propiedad, id=propiedad_id, dueño_id=dueño_id)

    propiedad.esta_publicado = not propiedad.esta_publicado
    propiedad.save()

    estado = "publicada" if propiedad.esta_publicado else "ocultada"
    messages.success(request, f'Propiedad {estado} correctamente.')
    return redirect('dashboard_dueno')
