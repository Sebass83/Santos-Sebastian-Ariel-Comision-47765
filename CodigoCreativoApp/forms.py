from django import forms
from CodigoCreativoApp.models import Blog
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