from django.http import request
from django.shortcuts import render, get_object_or_404,redirect
from .models import Servicios
from .forms import ServiciosForm

# Create your views here.
def demo(request):
    servicio = Servicios.objects.all( )
    contexto = {
        'servicio' : servicio
        } 
    return render(request, 'core/demo.html',contexto)

    
def proveedores(request):
    servicio = Servicios.objects.all( )
    contexto = {
        'servicio' : servicio
        } 
    return render(request, 'core/proveedores.html',contexto)


def crearServicio(request):
    if request.method == 'GET':
        form = ServiciosForm()
        contexto = {
            'form' : form
        }
    else:
        form = ServiciosForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('proveedores')
    return render(request, 'core/crear_servicio.html',{'form' : form})


def editarServicio(request,id):
    servicio = Servicios.objects.get(id_servicio= id)
    if request.method == 'GET':
        form = ServiciosForm(instance= servicio)
        contexto = {
            'form': form
        }
    else:
            form = ServiciosForm(request.POST, instance= servicio)
            if form.is_valid:
                form.save()
                return redirect('proveedores')
    return render(request, 'core/crear_servicio.html',{'form' : form})

def eliminarServicio(request,id):
    servicio = Servicios.objects.get(id_servicio=id)
    servicio.delete()
    return redirect('proveedores')




