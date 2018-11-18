from django import forms
from .models import Solicitudes, SolicitudesParametros
from django import forms


class DocumentosForm(forms.ModelForm):
    class Meta:
        model = SolicitudesParametros
        fields = ['archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels = {

        }

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=1000)
#     file = forms.FileField()

class SolicitudAdd(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['duracion', 'nombre', 'valor', 'descripcion', 'youtube', 'categoria']
        widgets = {   
            'content': forms.Textarea(attrs={'class':'ckeditor'}),
        }
        labels = {

        }