from django.db import models
from django.contrib.auth.models import User


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
    


    
