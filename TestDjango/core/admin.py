from django.contrib import admin
from .models import Servicios
from .models import Proveedor

# Register your models here.

admin.site.register(Servicios),
admin.site.register(Proveedor)
