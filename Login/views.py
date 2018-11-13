from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Usuario
from passlib.context import CryptContext
# Create your views here.

# Configuracion de la libraria de encryptacion para el password
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

# Creacion del objeto user del modelo de la bade de datos
user = Usuario()

def index(request):
    if request.method == "GET":
        return render(request, 'Login/index.html')
    

def perfil(request):

    if request.method == "GET":
        # Si el usuario esta logueado y recarga la pagina de perfil puede acceder a la misma
        # si no esta logueado lo redirije al index
        if "logueado" in request.session and request.session["logueado"] == True:
            dataUser = Usuario.objects.get(email=request.session["email"])
            return render(request, 'Login/perfil.html', {"usuario": dataUser})
        else:
            return render(request, 'Login/index.html')
            
    if request.method == "POST":

        if request.POST["fuente"] == "registro":
            # Se verifica si el nombre del usuario ya existe si es asi enviamos un mensaje
            if Usuario.objects.filter(nombre=request.POST["nombre"]).exists():
                mensaje = "Info: Este Nombre ya existe!"
                data = {"mensaje": mensaje, "email": request.POST["email"], "nombre": request.POST["nombre"]}
                return render(request, 'Login/index.html', data)
            # Se verifica si el email ya existe si es asi enviamos un mensaje
            if Usuario.objects.filter(email=request.POST["email"]).exists():
                mensaje = "Info: Este Email ya existe!"
                data = {"mensaje": mensaje, "email": request.POST["email"], "nombre": request.POST["nombre"]}
                return render(request, 'Login/index.html', data)
            
            # Si el email y el usuario no existe lo almacenamos en la DB
            user.nombre = request.POST["nombre"]
            user.email = request.POST["email"]
            # Aqui guardamos el password de usuario 
            # pero primero le encryptamos para no guardarlo como texto plano
            user.password = pwd_context.encrypt(request.POST["password"])
            user.save()

            # Una vez guardado el usuario lo tomamos de nuevo de la base de datos para enviarlo
            # a la view de perfil
            dataUser = Usuario.objects.get(email=request.POST["email"])
            request.session["logueado"] = True
            request.session["email"] = dataUser.email
            return render(request, 'Login/perfil.html', {"usuario": dataUser})
        
        if request.POST["fuente"] == "login":
            # Buscamos al usuario ya sea por nombre o por email
            if Usuario.objects.filter(email=request.POST["email"]).exists():
                dataUser = Usuario.objects.get(email=request.POST["email"])
            elif Usuario.objects.filter(nombre=request.POST["email"]).exists():
                dataUser = Usuario.objects.get(nombre=request.POST["email"])
            else:
                # Si no encontramos al usuario devolvemos un mensaje de error
                mensaje = "El nombre o el email no existe!"
                data = {"mensaje_login": mensaje, "email_login": request.POST["email"]}
                return render(request, 'Login/index.html', data)

            # verificamos que el password del usuario coincida con el que esta en la DB
            if pwd_context.verify(request.POST["password"], dataUser.password):
                request.session["logueado"] = True
                request.session["email"] = dataUser.email
                return render(request, 'Login/perfil.html', {"usuario": dataUser})
            else:
                mensaje = "Password errrado!"
                data = {"mensaje_login": mensaje, "email_login": request.POST["email"]}
                return render(request, 'Login/index.html', data)


def logout(request):

    if request.method == "GET":
        # Si el usuario esta logueado eliminamos la session del usuario y redirigimos al index
        if "logueado" in request.session and request.session["logueado"] == True:
            request.session.flush()
        return render(request, 'Login/index.html')


def editar(request):

    if request.method == "POST":
        if "logueado" in request.session and request.session["logueado"] == True:
            Usuario.objects.filter(id=request.POST["id"]).update(email=request.POST["email"],
                                                         nombre=request.POST["nombre"],
                                                         password=pwd_context.encrypt(request.POST["password"]))
            dataUser = Usuario.objects.get(id=request.POST["id"])
            return render(request, 'Login/perfil.html', {"usuario": dataUser})

    if request.method == "GET":
        if "logueado" in request.session and request.session["logueado"] == True:
            dataUser = Usuario.objects.get(email=request.session["email"])
            return render(request, 'Login/perfil.html', {"usuario": dataUser})
        else:
            return render(request, 'Login/index.html')
