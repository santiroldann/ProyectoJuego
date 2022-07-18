from django.db import models
from numpy import require
from django.contrib.auth.models import User

# Create your models here.
class ImgPerfil(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imgperfil/", blank=True, null=True)



class Jugador(models.Model):
    
    avatar = models.CharField(max_length=30)
    correo = models.EmailField(blank=True, null=True)
    juego = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Jugadores"
    
class Lider(models.Model):
    
    avatar = models.CharField(max_length=30)
    correo = models.EmailField(blank=True, null=True)
    juego = models.CharField(max_length=30)
    grupo = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Lideres"
              
class Juego(models.Model):
    
    juego = models.CharField(max_length=30)
    grupo = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Juegos"
