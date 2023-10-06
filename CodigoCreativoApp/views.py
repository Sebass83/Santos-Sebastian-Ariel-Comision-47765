
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CodigoCreativoApp.models import *


# Create your views here.
def inicio(request):
    data = Blog.objects.all()
    avatar = Avatar.objects.filter(user=request.user.id)
    if avatar:
        return render(request, 'index.html', {'data':data, "avatar":avatar[0].imagen.url})
    return render(request, 'index.html', {'data':data})
    


@login_required(login_url="/accounts/login/")
def crearBlog(request):
    avatar = Avatar.objects.filter(user=request.user.id)
   
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
            description = request.POST.get('description')
            author = request.user
            Blog.objects.create(title=title,subtitle=subtitle,description=description,author=author)
            return redirect('inicio')
        except Exception as e:
            print(e)
            return render(request, 'crear-blog.html', {'error': e})

    if avatar:
        return render(request, 'crear-blog.html', {"avatar":avatar[0].imagen.url})    
    return render(request, 'crear-blog.html')



