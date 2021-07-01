from django import forms
from django.forms import ModelForm
from .models import Servicios

class ServiciosForm (ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'