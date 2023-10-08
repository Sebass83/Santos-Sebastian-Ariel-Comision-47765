from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Blog(models.Model):

    def __str__(self):
        return f'Titulo: {self.title} - author: {self.author}'

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=400)
    entryDate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None) 
    imagen = models.ImageField(upload_to='post_image',default=None)
    body =  RichTextField(default=None)

class Mensajes(models.Model):
    de =  models.CharField(max_length=150)
    para = models.CharField(max_length=150)
    asunto = models.CharField(max_length=150)
    body =  RichTextField(default=None)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'de: {self.de} - para: {self.para} - asunto: {self.asunto}'

    


    
