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
            
#@method_decorator(login_required, name="dispatch")
#class MisOfertasRecibidasList(ListView):
#    template_name = "prestamos/inversionistassolicitudesrecibidas_list.html"
#
#    def get_queryset(self):
#        persona = self.request.user
#
#        return InversionistasSolicitudes.objects.filter(solicitud.solicitante=self.request.user)

@method_decorator(login_required, name="dispatch")
class MisOfertasList(ListView):
    template_name = "prestamos/inversionistassolicitudes_list.html"

    def get_queryset(self):
        return InversionistasSolicitudes.objects.filter(inversionista=self.request.user)