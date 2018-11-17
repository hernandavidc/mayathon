from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UploadFileForm

from .models import Solicitudes, NivelesDeRiesgo, Parametros, SolicitudesParametros
from .forms import SolicitudAdd

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

@login_required
def CompletarSolicitudesPost(request, solicitud):
    template_name = 'prestamos/solicitudescompletas_form.html'
    print(request.FILES)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        for f in request.FILES:
            if form.is_valid():
                handle_uploaded_file(f)
    else:
        form = UploadFileForm()

    solicitud = Solicitudes.objects.get(id=solicitud)
    parametros = SolicitudesParametros.objects.filter(solicitud=solicitud)
    return render(request, template_name, {'solicitud': solicitud, 'parametros': parametros}) 

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)