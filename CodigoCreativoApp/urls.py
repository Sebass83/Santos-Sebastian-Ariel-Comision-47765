from django.urls import path
from CodigoCreativoApp.views import inicio, crearBlog

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear-blog/", crearBlog , name="crearBlog")

]
