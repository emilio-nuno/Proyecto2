from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Choice
from django.contrib.auth.mixins import LoginRequiredMixin

#TODO Obligar al usuario a registrarse antes de acceder a la aplicación

class CrearRespuesta(LoginRequiredMixin, CreateView):
    model = Choice
    fields = '__all__'
    template_name = 'agregar_respuesta.html'

class DetalleRespuesta(LoginRequiredMixin, DetailView):
    model = Choice
    template_name = 'ver_respuesta.html'

class ActualizarRespuesta(LoginRequiredMixin, UpdateView):
    model = Choice
    fields = ['choice_text']
    template_name = 'editar_respuesta.html'

class EliminarRespuesta(LoginRequiredMixin, DeleteView):
    model = Choice
    template_name = 'eliminar_respuesta.html'
    success_url = reverse_lazy('index')
class ListarRespuestas(LoginRequiredMixin, ListView):
    model = Choice
    template_name ='listar_respuestas.html'
    def get_queryset(self):
        return Choice.objects.filter(user=self.request.user)