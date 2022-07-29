
from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    
    path("", inicio, name= "inicio"),
    path("login", login_request , name="login"),
    path("register", register_request , name="register"),
    path("logout", logout_request , name="logout"),
    path("editar_perfil", editar_perfil, name="editar_perfil"),
    path("agregar_imagen", agregar_imagen, name="agregar_imagen"),
    
    path("lideres/", lideres, name = "lideres"),
    path("jugadores/", jugadores, name= "jugadores"),
    path("juegos/", juegos, name= "juegos"),
    
    path("jugadores/list", JugadorList.as_view(), name="jugador_list"),
    path(r"^(?P<pk>\d+)$", JugadorDetail.as_view(), name="jugador_detail"),
    path(r"^nuevo$", JugadorCreate.as_view(), name="jugador_create"),
    path(r"^editar/(?P<pk>\d+)$", JugadorUpdate.as_view(), name="jugador_update"),
    path(r"^eliminar/(?P<pk>\d+)$", JugadorDelete.as_view(), name="jugador_delete"),
    
    path("lideres/list", LiderList.as_view(), name="lider_list"),
    path('lideres/<pk>', LiderDetail.as_view(), name="lider_detail"),
    path("lideres/nuevo", LiderCreate.as_view(), name="lider_create"),
    path("lideres/editar/<pk>", LiderUpdate.as_view(), name="lider_update"),
    path("lideres/eliminar/<pk>", LiderDelete.as_view(), name="lider_delete"),
    
    
    path("crear_juego/", crear_juego, name= "crear_juego"),
    path("crear_jugador/", crear_jugador, name= "crear_jugador"),
    path("crear_lider/", crear_lider, name= "crear_lider"),
    path("crear_post/", crear_post, name= "crear_post"),
    
    path("editar_juego/<juego_id>", editar_juego, name="editar_juego"),
    path("editar_jugador/<jugador_id>", editar_jugador, name="editar_jugador"),
    path("editar_lider/<lider_id>", editar_juego, name="editar_lider"),
    
    path("eliminar_juego/<juego_id>", eliminar_juego, name="eliminar_juego"),
    path("eliminar_jugador/<jugador_id>", eliminar_jugador, name="eliminar_jugador"),
    path("eliminar_lider/<lider_id>", eliminar_lider, name="eliminar_lider"),
    path("base/",base),
    
    path('cv/', cv, name="cv"),
    path('acerca/', acerca, name="acerca"),
    #path('crear_post/', crear_post, name="crear_post"),
    path('posts/', posts, name="posts"),
    path('post/', post, name="post"),
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),

]
