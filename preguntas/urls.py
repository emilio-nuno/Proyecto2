from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.CrearRespuesta.as_view(), name='index'),
    path('<int:pk>/', views.DetalleRespuesta.as_view(), name='detalle-respuesta'),
    path('actualizar/<int:pk>/', views.ActualizarRespuesta.as_view(), name='actualizar-respuesta'),
]