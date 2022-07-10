
from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    
    path("", inicio, name= "inicio"),
    
    path("lideres/", lideres, name = "lideres"),
    path("jugadores/", jugadores, name= "jugadores"),
    path("juegos/", juegos, name= "juegos"),
    
    path("jugador/list", JugadorList.as_view(), name="jugador_list"),
    path(r"^(?P<pk>\d+)$", JugadorDetail.as_view(), name="jugador_detail"),
    path(r"^nuevo$", JugadorCreate.as_view(), name="jugador_create"),
    path(r"^editar/(?P<pk>\d+)$", JugadorUpdate.as_view(), name="jugador_update"),
    path(r"^eliminar/(?P<pk>\d+)$", JugadorDelete.as_view(), name="jugador_delete"),
    
    path("lider/list", LiderList.as_view(), name="lider_list"),
    path(r"^(?P<pk>\d+)$", LiderDetail.as_view(), name="lider_detail"),
    path(r"^nuevo$", LiderCreate.as_view(), name="lider_create"),
    path(r"^editar/(?P<pk>\d+)$", LiderUpdate.as_view(), name="lider_update"),
    path(r"^eliminar/(?P<pk>\d+)$", LiderDelete.as_view(), name="lider_delete"),
    
    
    path("crear_juego/", crear_juego, name= "crear_juego"),
    path("crear_jugador/", crear_jugador, name= "crear_jugador"),
    path("crear_lider/", crear_lider, name= "crear_lider"),
    
    path("editar_juego/<juego_id>", editar_juego, name="editar_juego"),
    
    path("eliminar_juego/<juego_id>", eliminar_juego, name="eliminar_juego"),
    path("eliminar_jugador/<estudiante_id>", eliminar_jugador, name="eliminar_jugador"),
    path("base/",base),

]
