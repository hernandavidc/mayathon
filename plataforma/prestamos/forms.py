from django import forms
from .models import Solicitudes
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=1000)
    file = forms.FileField()

class SolicitudAdd(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['duracion', 'nombre', 'valor', 'descripcion', 'youtube', 'categoria']
        widgets = {   
            'content': forms.Textarea(attrs={'class':'ckeditor'}),
        }
        labels = {

        }