
from django import forms
from tabnanny import verbose

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