from django.urls import path
from .views import MisOfertasList, OfertarPrueba

inversionista_patterns = ([
    path('inversionista/', MisOfertasList.as_view(), name='listOfertas'),
    path('inversionista/<int:solicitud>/', OfertarPrueba.as_view(), name='ofertar'),
    path('solicitudes/', MisOfertasRecibidasList.as_view(), name='solicitudes'),
],'inversionistas')