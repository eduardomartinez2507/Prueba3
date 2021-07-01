from django.db import models

# Create your models here.

class Servicios (models.Model):
    id_servicio = models.IntegerField(primary_key=True, verbose_name="ID")
    nombre_servicio = models.CharField(max_length=50, verbose_name=" NOMBRE_SERVICIO")

    def __str__(self):
        return self.nombre_servicio
        
class Proveedor (models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name="rut_proveedor",default=0,null=False)
    nombre = models.CharField(max_length=50, verbose_name="nombre_o_razon",default='',null=False)
    descripcion = models.CharField(max_length=100, default='',verbose_name="descripcion",null=False)
    email = models.CharField(max_length=50, verbose_name="email",default='',null=False)
    telefono = models.CharField(max_length=20, verbose_name="telefono",default='',null=False)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    