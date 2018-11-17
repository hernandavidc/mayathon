from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Solicitudes
from .forms import SolicitudAdd

class SolicitudesList(ListView):
    model = Solicitudes
    template_name = "prestamos/list_solicitudes.html"

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

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            camara = form.save(commit=False)
            camara.save()
            return HttpResponseRedirect('/mis-proyectos/?ok')
        return render(request, self.template_name, {'form': form})
