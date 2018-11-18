from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

ESTADO_CHOICE = (
     ('a','Aceptado'),
     ('r','Rechazado'),
     ('p','Proceso'),
)

ESTADO_INVERSION = (
    ('s','Solicitado'),
    ('a','Aceptado'),
    ('r','Rechazado'),
    ('t','Inversión retornada'),
    ('z','Inversión realizada'),
    ('m','Inversión en mora'),
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

class NivelesDeRiesgo(models.Model):
    limiteInferior = models.IntegerField()
    limiteSuperior = models.IntegerField()
    riesgo = models.CharField(max_length=10)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2)

class Solicitudes(models.Model):
    fecha_inicio = models.DateField(null=True, blank=True)
    duracion = models.IntegerField()
    nombre = models.CharField(max_length=20)
    valor = models.IntegerField()
    valor_Faltante = models.IntegerField()
    descripcion = RichTextField(verbose_name="Contenido")
    youtube = models.URLField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=1, choices= ESTADO_CHOICE, default='p')
    solicitante = models.ForeignKey(User, related_name="get_solicitudes", on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    nivelDeRiesgo = models.ForeignKey(NivelesDeRiesgo, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Parametros(models.Model):
    nombre = models.TextField()
    valor = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class SolicitudesParametros(models.Model):
    solicitud = models.ForeignKey(Solicitudes, related_name='get_parametros', on_delete=models.PROTECT)
    parametro = models.ForeignKey(Parametros, on_delete=models.PROTECT)
    archivo = models.FileField(upload_to=custom_upload_to, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

class InversionistasSolicitudes(models.Model):
    inversionista = models.ForeignKey(User, on_delete=models.PROTECT)
    solicitud = models.ForeignKey(Solicitudes, on_delete=models.PROTECT)
    inversion = models.IntegerField()
    estado = models.CharField(max_length=1, choices= ESTADO_INVERSION, default='s')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
class Rankings(models.Model):
    monto = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)