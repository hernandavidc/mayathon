from django import forms
from .models import Solicitudes

class SolicitudAdd(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['duracion', 'nombre', 'valor', 'descripcion', 'youtube', 'estado', 'solicitante', 'categoria']
        widgets = {   
        }
        labels = {

        }