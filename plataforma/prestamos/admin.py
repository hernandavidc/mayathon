from django.contrib import admin
from .models import Solicitudes, Categorias, Parametros, Rankings, NivelesDeRiesgo, InversionistasSolicitudes

admin.site.register(Solicitudes)
admin.site.register(Categorias)
admin.site.register(Parametros)
admin.site.register(Rankings)
admin.site.register(NivelesDeRiesgo)
admin.site.register(InversionistasSolicitudes)
