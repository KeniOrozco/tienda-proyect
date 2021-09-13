from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('productos/', producto_list, name='productos'),
]