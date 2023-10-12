from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from CodigoCreativoApp.models import *
from CodigoCreativoApp.forms import *
from CodigoCreativoApp.helpers.helperPost import createPost, deletePost, editPost

# Create your views here.
def inicio(request):
    data = Blog.objects.all().order_by("-entryDate")   
    return render(request, "index.html", {"data": data})


@login_required(login_url="/accounts/login/")
def crearPost(request):
    return createPost(request)


@login_required(login_url="/accounts/login/")
def editarPost(request, id):
    return editPost(request, id)
    

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

def searchPost(request):  
    if request.method == 'POST' and request.POST['term']:
        term = request.POST['term'].strip()
        if len(term) > 0:
            results = Blog.objects.filter(body__icontains = term)
            print({'results':results})
            if results:
                if len(results) > 1:
                    return render(request, "posts.html", {"data": results, 'message': f'Se encontraron {len(results)} posts para la búsqueda: {term}'})
                else:
                    authorAvatar = Avatar.objects.filter(user= results[0].author.id)
                    if authorAvatar:    
                        return render(request, "post.html", {"data": results, 'authorAvatar': authorAvatar[0].imagen.url})
                    return render(request, "post.html", {"data": results})
        else:
            return render(request, "index.html", {"message":f'No se encontró resultado para {term}'})
    return redirect('inicio')

def getPerfil(request,user):
    usuario = User.objects.get(id = user)
    userAvatar = Avatar.objects.filter(user__exact= user)[0]
    urls = PerfilURLS.objects.filter(usuario__exact=user).last()

    return render(request, 'perfil.html',{'usuario':usuario or None,'userAvatar':userAvatar or None,'urls':urls or None})

@login_required(login_url="/accounts/login/")
def eliminarPost(request,id):
    return deletePost(request,id)
       
def sobreMi(request):
    return render(request, 'sobre-mi.html')

@login_required(login_url="/accounts/login/")
def setAvatar(request):
    if request.method == "POST":

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
            return redirect('inicio')
    
    form=SetAvatar()
    return render(request,'set-avatar.html',{'forms':form})


    

@login_required(login_url="/accounts/login/")
def inboxMsj(request):
    if request.method == 'GET':
        msj = Mensajes.objects.filter(para=request.user.username)
        if msj:
            return render(request, 'mis-mensajes.html', {'msj': msj})
        else:
            return render(request, 'mis-mensajes.html', {'message': 'No tienes mensajes'})

    
@login_required(login_url="/accounts/login/")
def sendMsj(request, destino):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            de = request.user.username
            para = destino
            asunto = form.cleaned_data['asunto']
            body =  form.cleaned_data['body']
            msj = Mensajes(de=de, para=para, asunto=asunto, body=body)
            msj.save()
            return render(request, 'enviar-mensaje.html',{'forms':form, 'message':'Mensaje enviado correctamente!','destino':destino})

        else:
            form = SendMessageForm()
            return render(request, 'enviar-mensaje.html',{'forms':form, 'error':'Algo salió mal!','destino':destino})
    form = SendMessageForm()
    return render(request, 'enviar-mensaje.html',{'forms':form, 'destino':destino})

@login_required(login_url="/accounts/login/")
def replyMsj(request, respoderA, asunto):
    enRespuesta = f'En respuesta a: {asunto}'
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            de = request.user.username
            para = respoderA
            asunto = form.cleaned_data['asunto']
            body =  form.cleaned_data['body']
            msj = Mensajes(de=de, para=para, asunto=asunto, body=body)
            msj.save()
            return render(request, 'responder-mensaje.html',{'forms':form, 'message':'Mensaje enviado correctamente!','respoderA': respoderA,'asunto': asunto})
        else:
            form = SendMessageForm(initial={'para':respoderA,'asunto':enRespuesta})
            return render(request, 'responder-mensaje.html',{'forms':form, 'error':'Algo salió mal!', 'respoderA': respoderA,'asunto': asunto})
    form = SendMessageForm(initial={'para':respoderA,'asunto':enRespuesta})
    return render(request, 'responder-mensaje.html',{'forms':form,'respoderA': respoderA,'asunto': asunto})
    
@login_required(login_url="/accounts/login/")
def deleteMsj(request,id):
    mensaje = Mensajes.objects.get(id=id)
    if mensaje.para == request.user.username:
        mensaje.delete()
        return redirect('inboxMsj')
    


    

    


        
