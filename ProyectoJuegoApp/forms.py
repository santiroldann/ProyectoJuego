
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
    
    roles = [("jugador", "Jugador"),("lider", "Lider")]
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    roles = forms.MultipleChoiceField(choices=roles, label="Roles", widget=forms.Select(choices=roles))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        
        help_texts = {k: "" for k in fields }
        
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password1 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput, required=False)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        
        help_texts = {k: "" for k in fields }