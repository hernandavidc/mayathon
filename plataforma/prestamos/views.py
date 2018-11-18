from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Solicitudes, NivelesDeRiesgo, Parametros, SolicitudesParametros
from .forms import SolicitudAdd, DocumentosForm

class SolicitudesList(ListView):
    model = Solicitudes
    template_name = "prestamos/list_solicitudes.html"

    def get_queryset(self):
        return Solicitudes.objects.filter(estado='p').exclude(nivelDeRiesgo=NivelesDeRiesgo.objects.get(id=4))

@method_decorator(login_required, name="dispatch")
class MeSolicitudesList(ListView):
    template_name = "prestamos/list_mesolicitudes.html"

    def get_queryset(self):
        return Solicitudes.objects.filter(solicitante=self.request.user)

@method_decorator(login_required, name="dispatch")
class SolicitudAdd(CreateView):
    model = Solicitudes
    form_class = SolicitudAdd
    success_url = reverse_lazy('prestamos:listMe')
    template_name = 'prestamos/solicitudes_form.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid() and len(Solicitudes.objects.filter(solicitante=self.request.user)) < 3:
            solicitud = form.save(commit=False)
            solicitud.solicitante = request.user
            solicitud.nivelDeRiesgo = NivelesDeRiesgo.objects.get(id=4)
            solicitud.valor_Faltante = solicitud.valor
            solicitud.save()
            parametros = Parametros.objects.all()
            for p in parametros:
                solicitudesParametros = SolicitudesParametros()
                solicitudesParametros.solicitud = solicitud
                solicitudesParametros.parametro = p
                solicitudesParametros.save()
            return HttpResponseRedirect('/mis-proyectos/?ok')
        return render(request, self.template_name, {'form': form, 'error':'No puedes publicar más de 3 solicitudes'})

@method_decorator(login_required, name="dispatch")
class solicitudesDetail(DetailView):
    model = Solicitudes

@login_required
def CompletarSolicitudes(request, solicitud):
    template_name = 'prestamos/solicitudescompletas_form.html'

    solicitud = Solicitudes.objects.get(id=solicitud)
    parametros = SolicitudesParametros.objects.filter(solicitud=solicitud)
    return render(request, template_name, {'solicitud': solicitud, 'parametros': parametros})

@method_decorator(login_required, name='dispatch')
class CompletarSolicitudesPost(UpdateView):
    template_name = 'prestamos/solicitudescompletas_form.html'
    
    form_class = DocumentosForm
    success_url = reverse_lazy('prestamos:guardar')

    def post(self, request, *args, **kwargs):
        #recuperamos el objeto que se va editar        
        form = self.form_class(request.POST)
        x = 10
        if form.is_valid():
            sp = form.save(commit=false)
            x = sp.solicitud.id
            sp.save()
        #p = SolicitudesParametros.objects.get(id=self.request.POST['id'])
        url = "/completar/" + str(x)
        return HttpResponseRedirect(url)
