from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from CodigoCreativoApp.forms import SetAvatar, SetPerfilURLS
from CodigoCreativoApp.models import Avatar, PerfilURLS
from AuthApp.forms import UserEditForm
import os


# Create your views here.


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data_username = form.cleaned_data.get("username")
            data_password = form.cleaned_data.get("password")

            user = authenticate(username=data_username, password=data_password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(
                    request,
                    "login.html",
                    {"form": form,"error": "Los datos ingresados son incorrectos"},
                )

        else:
            return render(request, "login.html", {"form": form,"error": "Error en el formulario"})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"registrarme.html",{"message": f"Te has registrado correctamente como: {username}"})
        else:
            return render(request,"registrarme.html",{"form": form,"error": "Los datos del formulario no son validos"})
    
    form = UserCreationForm()
    return render(request, "registrarme.html", {"form": form})
         

@login_required
def editarPerfil(request):
    usuario = request.user
    try:
        url = PerfilURLS.objects.filter(usuario=request.user)
     
    except:
        url = False


    if request.method == "POST":

        urlForm = SetPerfilURLS(request.POST)
        aEliminar = PerfilURLS.objects.filter(usuario__exact=request.user).last()
        
        if urlForm.is_valid():
            req = urlForm.cleaned_data
            if len(req) > 0:
                usuario = request.user
                if req['url_github']:
                    url_github = req['url_github']
                else:
                    url_github = ''
                if req['url_linkedin']:
                    url_linkedin = req['url_linkedin']
                else:
                    url_linkedin=''
                if req['url_personal']:
                    url_personal = req['url_personal']
                else:
                    url_personal=''
                urlsPerfil = PerfilURLS(usuario = usuario ,url_github = url_github ,url_linkedin = url_linkedin,url_personal = url_personal )
                if aEliminar:
                    aEliminar.delete()
                urlsPerfil.save()
                return redirect('EditarPerfil')
        
        miFormulario = UserEditForm(request.POST)
        try:
            if Avatar.objects.filter(user=request.user)[0]:
                oldAvatar = Avatar.objects.filter(user=request.user)[0]
                print({oldAvatar: oldAvatar})
                if oldAvatar:
                    img = str(oldAvatar.imagen.path)
                    if os.path.isfile(img):
                        os.remove(img)
                    oldAvatar.delete()
        except: 
            pass  

        form=SetAvatar(request.POST, request.FILES)
        if form.is_valid():
            usuario = request.user
            req = form.cleaned_data
            avatar = Avatar(user = usuario, imagen = req['imagen'])
            avatar.save()
            return redirect('EditarPerfil')
    
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]
            usuario.save()
            return redirect('Logout')
    else:
        print(url)
        if url:
            form=SetAvatar()
            miFormulario = UserEditForm(initial={"email": usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
            urlForm = SetPerfilURLS(initial={'url_github' : url[0].url_github, 'url_linkedin':url[0].url_linkedin, 'url_personal':url[0].url_personal})
        else:
            form=SetAvatar()
            miFormulario = UserEditForm(initial={"email": usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
            urlForm = SetPerfilURLS()

    return render(request,"editarPerfil.html",{"miformulario": miFormulario, "usuario": usuario,'forms':form, 'urlForm':urlForm} )
