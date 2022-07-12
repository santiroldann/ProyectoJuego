
from django import forms
from tabnanny import verbose
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        #help_texts = {k: "" for k in fields }