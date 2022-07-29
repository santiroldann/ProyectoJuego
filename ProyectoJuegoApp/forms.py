
from django import forms
from tabnanny import verbose
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextField
from django.forms import ModelForm
from ProyectoJuegoApp.models import ImgPerfil, Post


class NuevoJuego(forms.Form):
    
    juego = forms.CharField(max_length=30)
    grupo = forms.IntegerField(min_value=0)
    
class NuevoJugador(forms.Form):
    
    avatar = forms.CharField(max_length=30)
    correo = forms.EmailField()
    juego = forms.CharField(max_length=30)
    
class NuevoLider(forms.Form):
    
    avatar = forms.CharField(max_length=30)
    correo = forms.EmailField()
    juego = forms.CharField(max_length=30)
    grupo = forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    imgperfil = models.ImageField(upload_to='imgperfil/', null=True, blank=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        
        help_texts = {k: "" for k in fields }
        
class UserEditForm(UserCreationForm):
    
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    imgperfil = models.ImageField(upload_to='imgperfil/', null=True, blank=True)
    
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        
        help_texts = {k: "" for k in fields }
        
class ImgPerfilForm(forms.Form):
    
    imagen = forms.ImageField(label="imagen")
    
    class Meta:
        model = ImgPerfil
        fields = ['imagen'] 
        
class CrearPost(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria',)

class CreateMensajeForm(forms.Form):
    
    destinatario = forms.EmailField(label='Email', required=True, widget=forms.Select(choices=[('', 'Seleccione un destinatario')] + [(user.email, user.email) for user in User.objects.all()]))
    # email = forms.EmailField(label='Email', required=True)
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)     
