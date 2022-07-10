from django.db import models
from numpy import require

# Create your models here.
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
