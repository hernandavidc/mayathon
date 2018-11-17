from django.db import models
from django.contrib.auth.models import User 

ESTADO_CHOICE = (
     ('a','Aceptado'),
     ('r','Rechazado'),
     ('p','Proceso'),
)

def custom_upload_to(instance, filename):
    old_instance = SolicitudesParametros.objects.get(pk=instance.pk)
    old_instance.archivo.delete()
    return 'documentacion/' + filename

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Solicitudes(models.Model):
    fecha_inicio = models.DateField(null=True, blank=True)
    duracion = models.IntegerField()
    nombre = models.CharField(max_length=20)
    valor = models.IntegerField()
    descripcion = models.TextField()
    youtube = models.URLField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=1, choices= ESTADO_CHOICE)
    solicitante = models.ForeignKey(User, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Parametros(models.Model):
    nombre = models.TextField()
    valor = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

class SolicitudesParametros(models.Model):
    solicitud = models.ForeignKey(Solicitudes, on_delete=models.PROTECT)
    parametro = models.ForeignKey(Parametros, on_delete=models.PROTECT)
    archivo = models.FileField(upload_to=custom_upload_to, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

class InversionistasSolicitudes(models.Model):
    inversionista = models.ForeignKey(User, on_delete=models.PROTECT)
    solicitud = models.ForeignKey(Solicitudes, on_delete=models.PROTECT)
    inversion = models.IntegerField()
    estado = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
class Rankings(models.Model):
    monto = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)