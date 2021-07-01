from django.urls import path
from .views import demo,proveedores,crearServicio,editarServicio,eliminarServicio
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', demo, name= "demo" ),
    path('proveedores',proveedores, name= "proveedores"),
    path('crear_servicio',crearServicio, name='crear_servicio'),
    path('editar_servicio/<int:id>/',editarServicio , name='editar_servicio'),
    path('eliminar_servicio/<int:id>/',eliminarServicio , name='eliminar_servicio')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)