from django import forms
from CodigoCreativoApp.models import Avatar, Blog, Mensajes, PerfilURLS
from ckeditor.widgets import CKEditorWidget

class CrearPost(forms.Form):
    title = forms.CharField()
    subtitle = forms.CharField()
    description = forms.CharField()
    imagen = forms.ImageField()
    body =  forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = ['title','subtitle','description','imagen','body']
        exclude = ['entryDate','author']
 
class EditPost(forms.Form):
    title = forms.CharField()
    subtitle = forms.CharField()
    description = forms.CharField()
    body =  forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = ['title','subtitle','description','body']
        exclude = ['entryDate','author','imagen']

class SetAvatar(forms.Form):
    imagen = forms.ImageField()
    
    class Meta:
        model = Avatar
        fields = ['imagen']
        exclude = ['user']

class SendMessageForm(forms.Form):
   
    asunto = forms.CharField(max_length=150)
    body =  forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Mensajes
        fields = ['asunto', 'body']
        exclude = ['de','param'] 

class SetPerfilURLS(forms.Form):
    url_github = forms.URLField(required=False)
    url_linkedin= forms.URLField(required=False)
    url_personal= forms.URLField(required=False)
    class Meta:
        model = PerfilURLS
        fields = ['url_github', 'url_linkedin', 'url_personal']




    


