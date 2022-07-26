from ast import If
from lzma import FORMAT_ALONE
import re
from django.shortcuts import redirect, render

from django.http import HttpResponse
from requests import request
from ProyectoJuegoApp.models import *
from .forms import *
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy 
 
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

page_title = "Call Of Duty"

base_context = {
    'page_title': page_title,
}

def inicio(request):
    
    if request.user.is_authenticated:
         try:
            imgperfil = ImgPerfil.objects.get(usuario=request.user)
            url = imgperfil.imagen.url
         except:
            url = "/media/avatar/generica.png"
            
         return render(request,"index1.html",{"url":url})
        
    
    return render(request,"index1.html",{})

    
def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            
            else:
                return redirect("login")
            
        else:
            return redirect("login")
         
    form = AuthenticationForm()   
    
    return render(request, "login.html",{"form":form})

def register_request(request):
    
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("passsword1")
            
            form.save()
            user = authenticate(username=username, password=password)
           
            if user is not None:
              login(request, user)
              return redirect("inicio")
        
            else:
              return redirect("login")
        
        return render(request,"register.html",{"form":form})
    
    form = UserRegisterForm()
    
    return render(request, "register.html",{"form":form})  

def logout_request(request):
    logout(request)
    return redirect("inicio")
 
@login_required 
def editar_perfil(request):
    
    user = request.user
    
    try:
        imgperfil = ImgPerfil(usuario=user)
    except:
        imgperfil = ImgPerfil(usuario=user)
        imgperfil.save()
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            imgperfil.imagen = info["imagen"]
            
            user.save()
            imgperfil.save()
            
            return redirect("inicio")
    
        else:
            return render(request, "editar_perfil.html",{"form":form}) 
        
    else:
        form = UserEditForm(initial={"email":user.email,"first_name":user.first_name,"last_name":user.last_name, "imagen":imgperfil.imagen})
        
    return render(request,"editar_perfil.html",{"form":form})
 
@login_required
def agregar_imagen(request):
    
    if request.method == "POST":
        
        form = ImgPerfilForm(request.POST, request.FILES)
    
        if form.is_valid():
        
         user = User.objects.get(username=request.user.username)
        
         imgperfil = ImgPerfil(usuario=user, imagen=form.cleaned_data["imagen"])
        
         imgperfil.save()
    
        
         return redirect("inicio")
    
    else:
        form = ImgPerfilForm()
        
    return render(request,"agregar_imagen.html",{"form":form})
        
    
def crear_juego(request):
    
    if request.method == "POST":
        
        formulario = NuevoJuego(request.POST)
        
        if formulario.is_valid():
            
            info_juego = formulario.cleaned_data
        
            juego = Juego(juego = info_juego["juego"], grupo =int(info_juego["grupo"]))
        
            juego.save()
        
        
            return redirect("juegos") 
    
        else: 
          return render(request, "formulario_juego.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJuego()
        
        return render(request, "formulario_juego.html",{"form":formulariovacio})
    
def eliminar_juego(request,juego_id):
    
    juego = Juego.objects.get(id=juego_id)
    juego.delete()
    
    return redirect("juegos")

def editar_juego(request,juego_id):
    
    juego = Juego.objects.get(id=juego_id)
    
    if request.method == "POST":
        
        formulario = NuevoJuego(request.POST)
        
        if formulario.is_valid():
            
            info_juego = formulario.cleaned_data
            
            juego.juego = info_juego["juego"]
            juego.grupo = info_juego["grupo"]
            juego.save()
            
            return redirect("juegos")
            
            
    formulario = NuevoJuego(initial={"juego":juego.juego, "grupo":juego.grupo})
      
    return render(request,"formulario_juego.html",{"form":formulario})
         
def crear_jugador(request):
    
    if request.method == "POST":
        
        formulario = NuevoJugador(request.POST)
        
        if formulario.is_valid():
            
            info_jugador = formulario.cleaned_data
        
            jugador = Jugador(avatar = info_jugador["avatar"], correo = info_jugador["correo"], juego = info_jugador["juego"])
        
            jugador.save()
        
        
            return redirect("jugadores") 
    
        else: 
          return render(request, "formulario_jugador.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoJugador()
    
        
        return render(request, "formulario_jugador.html",{"form":formulariovacio})
    
def eliminar_jugador(request,jugador_id):
    
    jugador = Jugador.objects.get(id=jugador_id)
    jugador.delete()
    
    return redirect("jugadores")

def crear_lider(request):
    
    if request.method == "POST":
        
        formulario = NuevoLider(request.POST)
        
        if formulario.is_valid():
            
            info_lider = formulario.cleaned_data
        
            lider = Lider(avatar = info_lider["avatar"], correo = info_lider["correo"], juego = info_lider["juego"], grupo =int(info_lider["grupo"]))
        
            lider.save()
        
        
            return redirect("lideres") 
    
        else: 
          return render(request, "formulario_lider.html",{"form":formulariovacio})
        
    else: 
        
        formulariovacio = NuevoLider()
        
        return render(request, "formulario_lider.html",{"form":formulariovacio})   

def editar_jugador(request, jugador_id):
    
    jugador = Juego.objects.get(id=jugador_id)
    
    if request.method == "POST":
        
        formulario = NuevoJugador(request.POST)
        
        if formulario.is_valid():
            
            info_jugador = formulario.cleaned_data
            
            jugador.avatar = info_jugador["avatar"]
            jugador.correo = info_jugador["correo"]
            jugador.juego = info_jugador["juego"]
            jugador.save()
            
            return redirect("juegos")
            
            
    formulario = NuevoJugador(initial={"avatar":jugador.avatar, "correo":jugador.correo, "juego":jugador.juego})
      
    return render(request,"formulario_jugador.html",{"form":formulario})

def eliminar_lider(request,jugador_id):
    
    jugador = Jugador.objects.get(id=jugador_id)
    jugador.delete()
    
    return redirect("jugadores")
    

class JugadorList(ListView):
        
      model = Jugador
      template_name = "jugador_list.html"
   
class JugadorDetail(DetailView):
     
     model = Jugador
     template_name = "jugador_detail.html"  
        
class JugadorCreate(CreateView):
     
     model = Jugador
     success_url = "/juegoapp/jugador/list"
     fields = ["avatar", "correo", "juego"]
     
class JugadorUpdate(UpdateView):
   
     model = Jugador
     success_url = "/juegoapp/jugador/list"
     fields = ["avatar", "correo", "juego"]
     
class JugadorDelete(DeleteView):
     
     model = Jugador
     success_url = "/juegoapp/jugador/list"
     
def lideres(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            
            lideres = Lider.objects.filter(Q(avatar__icontains=search) | Q(juego__icontains=search) | Q(grupo__icontains=search)).values()
    
            return render(request, "lideres1.html",{"lideres":lideres, "search":True, "busqueda":search})

    lideres = Lider.objects.all()
    
    return render(request,"lideres1.html",{"lideres":lideres})

class LiderList(LoginRequiredMixin,ListView):
        
      model = Lider
      template_name = "lider_list.html"
   
class LiderDetail(DetailView):
     
     model = Lider
     template_name = "lider_detail.html"  
        
class LiderCreate(CreateView):
     
     model = Jugador
     success_url = "/juegoapp/list"
     fields = ["avatar", "correo", "juego", "grupo"]
     
class LiderUpdate(UpdateView):
   
     model = Lider
     success_url = "/juegoapp/list"
     fields = ["avatar", "correo", "juego", "grupo"]
     
class LiderDelete(DeleteView):
     
     model = Lider
     success_url = "/juegoapp/list"
    
def jugadores(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            
            jugadores = Jugador.objects.filter(avatar__icontains=search)
    
            return render(request, "jugadores1.html",{"jugadores":jugadores, "search":True, "busqueda":search})

    jugadores = Jugador.objects.all()
    
    return render(request,"jugadores1.html",{"jugadores":jugadores})


def juegos(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
        
         juegos = Juego.objects.filter(Q(juego__icontains=search) | Q(grupo__icontains=search)).values()
        
         return render(request,"juegos1.html",{"juegos":juegos, "search":True, "busqueda":search})
    
    
    juegos = Juego.objects.all()
    
    return render(request,"juegos1.html",{"juegos":juegos})
     
def base(request):
    
    return render(request,"base1.html",{})

def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "acerca.html", {})

def post(request):

    return render(request, "post.html", {})

def post2(request):

    return render(request, "post2.html", {})

def post3(request):

    return render(request, "post3.html", {})

def post4(request):

    return render(request, "post4.html", {})

def enviar_mensaje(request):
    if request.method == "POST":
        form = CreateMensajeForm(request.POST)
        if form.is_valid():
            info  = form.cleaned_data
            nuevo_mensaje = Mensaje(remitente=request.user,destinatario=User.objects.get(email=info["destinatario"]), mensaje = info["mensaje"])
            nuevo_mensaje.save()
            # form.save()
            messages.success(request, "Mensaje enviado!")
            return redirect("inicio")
        else:
            messages.error(request, "Error al enviar el mensaje!")
            return redirect("inicio")
    else:
        form = CreateMensajeForm()
        base_context.update({"form":form})
        return render(request,"mensaje.html", base_context)
