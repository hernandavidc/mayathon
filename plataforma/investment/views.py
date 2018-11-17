from django.shortcuts import render
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from prestamos.models import InversionistasSolicitudes
from prestamos.models import Solicitudes
from .forms import Ofertar

@method_decorator(login_required, name="dispatch")
class OfertarPrueba(CreateView):
    model = InversionistasSolicitudes
    form_class = Ofertar
    success_url = reverse_lazy('inversionistas:listOfertas')
    
    # def get_context_data(self, **kwargs):
    #     contexto = super(OfertarPrueba, self).get_context_data(**kwargs)
    #     print(contexto.path)
    #     print("================")
    #     return contexto
    def post(self,request, *args, **kwargs):
        print(request.POST)
        form=self.form_class(request.POST)
        if form.is_valid():
            inversion = form.save(commit=False)
            print()
            inversion.inversionista=request.user
            inversion.solicitud = Solicitudes.objects.get(id=request.POST["id"])
            inversion.save()#
            return HttpResponseRedirect('/inversionista/?ok')#
        return render(request, self.template_name, {'form': form})#



@method_decorator(login_required, name="dispatch")
class Ofertar(CreateView):
    model= InversionistasSolicitudes
    form_class= Ofertar
    success_url = reverse_lazy('inversionistas:listOfertas')

    # def post(self,request, *args, **kwargs):
    #     print(request.POST)
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         inversion = form.save(commit=False)
    #         print()
    #         inversion.inversionista=request.user
    #         inversion.solicitud = request.get["id"]##
    #         inversion.save()#
    #         return HttpResponseRedirect('/mis-proyectos/?ok')#
    #     return render(request, self.template_name, {'form': form})#
            
@method_decorator(login_required, name="dispatch")
class MisOfertasRecibidasList(ListView):
    template_name = "prestamos/inversionistassolicitudesrecibidas_list.html"

    def get_queryset(self):
        solicitudes = self.request.user.get_solicitudes.all()

        return InversionistasSolicitudes.objects.filter(solicitud__in=solicitudes)

@method_decorator(login_required, name="dispatch")
class MisOfertasList(ListView):
    template_name = "prestamos/inversionistassolicitudes_list.html"

    def get_queryset(self):
        return InversionistasSolicitudes.objects.filter(inversionista=self.request.user)

@login_required
def ofertaRecibidaAdd(request, pk):
    solicitudFinanciacion = InversionistasSolicitudes.objects.get(id = pk)
    proyecto = solicitudFinanciacion.solicitud
    inversor = solicitudFinanciacion.inversionista
    solicitudFinanciacion.estado = 'a'
    solicitudFinanciacion.save()
    proyecto.valor_Faltante -= solicitudFinanciacion.inversion
    proyecto.save()
    inversor.notificacion = 1
    inversor.save()

    return HttpResponseRedirect('/solicitudes/?ok')

@login_required
def ofertaRecibidaDecline(request, pk):
    solicitudFinanciacion = InversionistasSolicitudes.objects.get(id = pk)
    inversor = solicitudFinanciacion.inversionista
    solicitudFinanciacion.estado = 'r'
    solicitudFinanciacion.save()
    inversor.notificacion = 1
    inversor.save()

    return HttpResponseRedirect('/solicitudes/?ok-n')
