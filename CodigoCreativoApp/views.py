from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CodigoCreativoApp.models import *
from CodigoCreativoApp.forms import *
import os


# Create your views here.
def inicio(request):
    data = Blog.objects.all().order_by("-entryDate")   
    return render(request, "index.html", {"data": data})


@login_required(login_url="/accounts/login/")
def crearPost(request):
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
       
            return render(
                request,
                "index.html",
                {"data": data, "message": f"Se creo con éxito el post {title}."}
            )
    else:
        forms = CrearPost()

    return render(request, "crear-blog.html", {"forms": forms})


@login_required(login_url="/accounts/login/")
def editarPost(request, id):
    postOriginal = Blog.objects.get(id=id)

    if postOriginal.author == request.user:
        if request.method == 'POST':
            form = EditPost(request.POST)
            if form.is_valid():
                editedPost = form.cleaned_data
                postOriginal.title = editedPost['title']
                postOriginal.subtitle = editedPost['subtitle']
                postOriginal.description = editedPost['description']
                postOriginal.body = editedPost['body']
                postOriginal.save()

                data = Blog.objects.filter(author=request.user)
                if data:
                    return render(request, "mis-post.html", {"data": data, 'message': 'Post editado y guardado con éxito'})
                else:
                    return render(request, "mis-post.html", {'message': 'Post editado y guardado con éxito'})
        form = EditPost(initial={'title':postOriginal.title, 'subtitle':postOriginal.subtitle, 'description':postOriginal.description, 'body':postOriginal.body})
        return render(request, "editar-blog.html", {"forms": form, 'id': id})
    else:
        data = Blog.objects.filter(author=request.user)
        if data:
            return render(request, "mis-post.html", {"data": data, 'error': 'El post que quieres editar no te pertenece o no existe'})
        else:
            return render(request, "mis-post.html", {'error': 'El post que quieres editar no te pertenece o no existe'})
        


    



def misPosts(request):
    data = Blog.objects.filter(author=request.user)


    if request.method == "GET":
        if data:
            return render(request, "mis-post.html", {"data": data})
        else:
            return render(request, "mis-post.html", {"error": "Sin post propios."})


def getPost(request, id):
    data = Blog.objects.filter(id=id)
    authorAvatar = Avatar.objects.filter(user= data[0].author.id)
    
    if request.method == "GET":
        if data:
            if authorAvatar:    
                return render(request, "post.html", {"data": data, 'authorAvatar': authorAvatar[0].imagen.url})
            return render(request, "post.html", {"data": data})
        else:
            return render(
                request, "post.html", {"error": f"No se encontró post con el id: {id}"}
            )


def allPosts(request):
    data = Blog.objects.all()

    return render(request, "posts.html", {"data": data})

@login_required(login_url="/accounts/login/")
def setAvatar(request):
    if request.method == "POST":
        form=SetAvatar(request.POST, request.FILES)
        if form.is_valid():
            usuario = request.user
            req = form.cleaned_data
            avatar = Avatar(user = usuario, imagen = req['imagen'])
            avatar.save()
           
            
            return render(request,'index.html',{'message':f'Se asigno con éxito el avatar a {usuario}'})
    else:
        form=SetAvatar()
    return render(request,'set-avatar.html',{'forms':form})

@login_required(login_url="/accounts/login/")
def eliminarPost(request,id):
    if request.method == 'GET':
        try:
            post = Blog.objects.get(id=id)
        except Exception as e:
            data = Blog.objects.filter(author=request.user)
            if data:
                return render(request, "mis-post.html", {"data": data, "error": "El post que intentas eliminar no existe"})
            else:
                return render(request, "mis-post.html", {"error": "Sin post propios. El post que intentas eliminar no existe"})

        if post.author == request.user:
            img = str(post.imagen.path)
            if os.path.isfile(img):
                os.remove(img)
            
            post.delete()
            data = Blog.objects.filter(author=request.user)
            return redirect('misPosts')
        else:
            if data:
                return render(request, "mis-post.html", {"data": data, "error": "El post que intentas eliminar, no te pertenece."})
            else:
                return render(request, "mis-post.html", {"error": "Sin post propios. El post que intentas eliminar, no te pertenece."})



