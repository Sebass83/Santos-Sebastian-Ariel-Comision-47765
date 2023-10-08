from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CodigoCreativoApp.models import *
from CodigoCreativoApp.forms import *


# Create your views here.
def inicio(request):
    data = Blog.objects.all().order_by("-entryDate")
    avatar = Avatar.objects.filter(user=request.user.id)
    if avatar:
        return render(
            request, "index.html", {"data": data, "avatar": avatar[0].imagen.url}
        )
    return render(request, "index.html", {"data": data})


@login_required(login_url="/accounts/login/")
def crearBlog(request):
    avatar = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        forms = CrearPost(request.POST, request.FILES)
        print(forms.is_valid())

        if forms.is_valid():
            print("Success")
            title = forms.cleaned_data["title"]
            subtitle = forms.cleaned_data["subtitle"]
            description = forms.cleaned_data["description"]
            imagen = forms.cleaned_data["imagen"]
            body = forms.cleaned_data["body"]
            author = request.user
            post = Blog(
                title=title,
                subtitle=subtitle,
                description=description,
                imagen=imagen,
                body=body,
                author=author,
            )
            post.save()

            data = Blog.objects.all().order_by("-entryDate")
            avatar = Avatar.objects.filter(user=request.user.id)
            if avatar:
                return render(
                    request,
                    "index.html",
                    {
                        "data": data,
                        "avatar": avatar[0].imagen.url,
                        "message": f"Se creo con éxito el post {title}.",
                    },
                )
            return render(
                request,
                "index.html",
                {"data": data, "message": f"Se creo con éxito el post {title}."},
            )
    else:
        forms = CrearPost()

    if avatar:
        return render(
            request, "crear-blog.html", {"avatar": avatar[0].imagen.url, "forms": forms}
        )
    return render(request, "crear-blog.html", {"forms": forms})


def misPosts(request):
    data = Blog.objects.filter(author=request.user)
    avatar = Avatar.objects.filter(user=request.user.id)

    if request.method == "GET":
        if data:
            if avatar:
                return render(
                    request,
                    "mis-post.html",
                    {"data": data, "avatar": avatar[0].imagen.url},
                )
            return render(request, "mis-post.html", {"data": data})
        else:
            if avatar:
                return render(
                    request,
                    "mis-post.html",
                    {"Mensaje": "Sin post propios.", "avatar": avatar[0].imagen.url},
                )
            return render(request, "mis-post.html", {"Mensaje": "Sin post propios."})


def getPost(request, id):
    data = Blog.objects.filter(id=id)
    avatar = Avatar.objects.filter(user=request.user.id)

    print(data[0].imagen.url)

    if request.method == "GET":
        if data:
            if avatar:
                return render(
                    request, "post.html", {"data": data, "avatar": avatar[0].imagen.url}
                )
            return render(request, "post.html", {"data": data})
        else:
            return render(
                request, "post.html", {"error": f"No se encontro post con el id: {id}"}
            )


def allPosts(request):
    data = Blog.objects.all()
    avatar = Avatar.objects.filter(user=request.user.id)
    if avatar:
        return render(
            request, "posts.html", {"data": data, "avatar": avatar[0].imagen.url}
        )
    return render(request, "posts.html", {"data": data})
