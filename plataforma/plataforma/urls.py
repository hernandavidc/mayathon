"""plataforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from prestamos.urls import prestamos_patterns
from investment.urls import inversionista_patterns
from .views import HomePageView

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('perfiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    path('', include(prestamos_patterns)),
    path('',include(inversionista_patterns)),
    #blog
    path('blog/', include('blog.urls')),
    #Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('cuenta/', include('registration.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.DOCUMENTACION_URL, document_root=settings.DOCUMENTACION_ROOT)
