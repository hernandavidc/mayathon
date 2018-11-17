from django.urls import path
from .views import SolicitudesList, MeSolicitudesList, SolicitudAdd

prestamos_patterns = ([
    path('proyectos/', SolicitudesList.as_view(), name='list'),
    path('mis-proyectos/', MeSolicitudesList.as_view(), name='listMe'),
#    path('<int:pk>/', ThreadDetail.as_view(), name='detail'),
    path('proyecto/add/', SolicitudAdd.as_view(), name='add'),
], 'prestamos')