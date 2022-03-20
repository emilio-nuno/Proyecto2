from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarRespuestas.as_view(), name='index'),
    path('agregar/', views.CrearRespuesta.as_view(), name='agregar-respuesta'),
    path('<int:pk>/', views.DetalleRespuesta.as_view(), name='detalle-respuesta'),
    path('actualizar/<int:pk>/', views.ActualizarRespuesta.as_view(), name='actualizar-respuesta'),
    path('eliminar/<int:pk>/', views.EliminarRespuesta.as_view(), name='eliminar-respuesta'),
    path('registro/', views.CrearUsuario.as_view(), name='agregar-usuario'),
]