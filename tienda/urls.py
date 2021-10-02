from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('tienda/carrito', views.CarritoView.as_view(), name='carrito'),
    path('productos/', producto_list, name='productos'),
    path('productos/<int:pk>', producto_detalle, name='productos_detalle'),
]