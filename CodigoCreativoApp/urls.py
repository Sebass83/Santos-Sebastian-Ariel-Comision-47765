from django.urls import path
from CodigoCreativoApp.views import *

urlpatterns = [
    #Leer
    path("", inicio, name="inicio"),
    path("mis-post/", misPosts, name="misPosts"),
    path("post/<int:id>", getPost , name="getPost"),
    path("blogs/", allPosts, name="allPosts"),
    #Crear
    path("crear-blog/", crearPost , name="crearBlog"),
    #Editar
    path("editar-post/<int:id>", editarPost , name="editarPost"),
    #Eliminar
    path("eliminar-post/<int:id>", eliminarPost, name="eliminarPost"),

    #Asignar Avatar
    path('set-avatar/', setAvatar, name="setAvatar"),

    #Enviar mensajes
    path('enviar-mensaje/<str:destino>', sendMsj, name="sendMsj")
]
