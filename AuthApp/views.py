from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from AuthApp.form import UserEditForm


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
                return render(request, "index.html", {"user": data_username})
            else:
                return render(
                    request,
                    "login.html",
                    {"error": "Los datos ingresados son incorrectos"},
                )

        else:
            return render(request, "login.html", {"error": "Error en el formulario"})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(
                request,
                "registrarme.html",
                {
                    "form": form,
                    "mensaje": f"Te has registrado correctamente como: {username}",
                },
            )

    else:
        form = UserCreationForm()

    return render(request, "registrarme.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]

            usuario.save()

            return render(request, "logout.html")

    else:
        miFormulario = UserEditForm(initial={"email": usuario.email})

    return render(
        request,
        "editarPerfil.html",
        {"miformulario": miFormulario, "usuario": usuario},
    )
