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
    #Buscar
    path("buscar-post/", searchPost, name="searchPost"),

    #Asignar Avatar
    path('set-avatar/', setAvatar, name="setAvatar"),

    #Enviar mensajes
    path('enviar-mensaje/<str:destino>', sendMsj, name="sendMsj"),
    #Enviar mensajes respoderA, asunto
    path('reponder-mensaje/<str:respoderA>/<str:asunto>', replyMsj, name="replyMsj"),
    #Ver mensaje
    path('mis-mensajes/',inboxMsj, name="inboxMsj"),
    #No lo elimina, lo pone no visible, esto para evitar malos entendidos, para eliminar los mensajes, se tiene que hacer desde el administrador.
    path('eliminar-mensaje/<int:id>,',deleteMsj, name="deleteMsj"),

    #Ver perfil
    path('perfil/<int:user>',getPerfil, name="getPerfil")



]
