
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from CodigoCreativoApp.models import *


# Create your views here.
def inicio(request):
    data = Blog.objects.all()
    
    return render(request, 'index.html', {'data':data})

@login_required(login_url="/accounts/login/")
def crearBlog(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            subtitle = request.POST.get('subtitle')
            description = request.POST.get('description')
            author = request.user
            Blog.objects.create(title=title,subtitle=subtitle,description=description,author=author)
            return render(request, 'inicio.html')
        except Exception as e:
            print(e)
            return render(request, 'crear-blog.html', {'error': e})
        
    return render(request, 'crear-blog.html')
