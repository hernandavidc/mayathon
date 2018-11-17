from django.urls import path
from .views import ofertaRecibidaDecline, ofertaRecibidaAdd, MisOfertasList, OfertarPrueba, MisOfertasRecibidasList

inversionista_patterns = ([
    path('inversionista/', MisOfertasList.as_view(), name='listOfertas'),
    path('inversionista/<int:solicitud>/', OfertarPrueba.as_view(), name='ofertar'),
    path('solicitudes/ok/<int:pk>/', ofertaRecibidaAdd, name='add'),
    path('solicitudes/no/<int:pk>/', ofertaRecibidaDecline, name='decline'),
    path('solicitudes/', MisOfertasRecibidasList.as_view(), name='solicitudes'),
],'inversionistas')