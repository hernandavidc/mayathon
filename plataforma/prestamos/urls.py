from django.urls import path
from .views import SolicitudesList, MeSolicitudesList, SolicitudAdd, solicitudesDetail, CompletarSolicitudes, CompletarSolicitudesPost

prestamos_patterns = ([
    path('proyectos/', SolicitudesList.as_view(), name='list'),
    path('mis-proyectos/', MeSolicitudesList.as_view(), name='listMe'),
    path('proyecto/<int:pk>/', solicitudesDetail.as_view(), name='Detail'),
    path('proyecto/add/', SolicitudAdd.as_view(), name='add'),
    path('completar/<int:solicitud>/', CompletarSolicitudes, name='completar'),
    path('guardar/', CompletarSolicitudesPost.as_view(), name='guardar')
], 'prestamos')