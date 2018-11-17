from django.contrib import admin
from .models import Solicitudes, Categorias, Parametros, Rankings, NivelesDeRiesgo

admin.site.register(Solicitudes)
admin.site.register(Categorias)
admin.site.register(Parametros)
admin.site.register(Rankings)
admin.site.register(NivelesDeRiesgo)
