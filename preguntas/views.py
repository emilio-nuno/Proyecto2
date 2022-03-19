from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Choice

class CrearRespuesta(CreateView):
    model = Choice
    fields = '__all__'
    template_name = 'agregar_respuesta.html'

class DetalleRespuesta(DetailView):
    model = Choice
    template_name = 'ver_respuesta.html'

class ActualizarRespuesta(UpdateView):
    model = Choice
    fields = ['choice_text']
    template_name = 'editar_respuesta.html'


@login_required
def index(request):
    return HttpResponse('Hola Mundo de las Preguntas')