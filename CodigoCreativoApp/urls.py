from django.urls import path
from CodigoCreativoApp.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear-blog/", crearBlog , name="crearBlog"),
    path("mis-post/", misPosts, name="misPosts"),
    path("post/<int:id>", getPost , name="getPost"),
    path("blogs/", allPosts, name="allPosts"),
]
