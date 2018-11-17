from django import forms
from prestamos.models import InversionistasSolicitudes

class Ofertar(forms.ModelForm):
    class Meta:
        model = InversionistasSolicitudes
        fields = ['inversion']
        widgets ={
            
        }
        labels ={
            
        }