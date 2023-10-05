from django.urls import path
from AuthApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"), 
    path('registrame/', views.register, name="Registrame"),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name="Logout"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"), 
]