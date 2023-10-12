from django.urls import path
from AuthApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="Login"), 
    path('registrame/', register, name="Registrame"),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name="Logout"),
    path('editarPerfil/', editarPerfil, name="EditarPerfil")
]