from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.CrearRespuesta.as_view(), name='index'),
    path('<pk>/', views.DetalleRespuesta.as_view(), name='detalle-respuesta'),
]