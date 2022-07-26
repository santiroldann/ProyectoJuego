from email.policy import default
from tabnanny import verbose
from django.db import models
from numpy import require
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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
        
class Post(models.Model):
    
    id = models.AutoField(primary_key = True)
    titulo = models.CharField("Titulo", max_length= 90, blank = False, null= False)
    slug = models.CharField("Slug", max_length= 100, blank= False, null = False)
    descripcion = models.CharField("Descripcion", max_length= 110, blank = False, null= False)
    contenido = RichTextField("Contenido", default = "Some string")
    imagen = models.URLField(max_length= 255, blank= 255, null= False)
    autor = models.ForeignKey("Jugador", on_delete = models.CASCADE)
    categoria = models.ForeignKey("Juego", on_delete = models.CASCADE)
    estado = models.BooleanField("Publicado/No Publicado", default= True)
    fecha_creacion = models.DateField("Fecha de Creación", auto_now = False, auto_now_add = True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.titulo

class Mensaje(models.Model):

    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')

    mensaje = models.TextField(max_length=500, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje