from django.urls import path
from .views import SolicitudesList, MeSolicitudesList, SolicitudAdd, solicitudesDetail

prestamos_patterns = ([
    path('proyectos/', SolicitudesList.as_view(), name='list'),
    path('mis-proyectos/', MeSolicitudesList.as_view(), name='listMe'),
    path('proyecto/<int:pk>/', solicitudesDetail.as_view(), name='Detail'),
    path('proyecto/add/', SolicitudAdd.as_view(), name='add'),
], 'prestamos')