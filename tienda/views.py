from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import datetime
import json
from django.views import generic
from django.db.models import Q
from .models import Producto, OrdenItem, Direccion, Orden, Categoria
from django.shortcuts import get_object_or_404, reverse, redirect
from .forms import AgregarAlCarrito
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.core.paginator import Paginator

#listado del producto
def producto_list(request): 
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()
    paginator = Paginator(producto,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tienda/productos.html', {'productos': producto, 'categorias': categoria, 'productos': page_obj})

#obtener el detalle de un producto
def producto_detalle(request,pk): 
    producto = Producto.objects.get(pk=pk)

    form = AgregarAlCarrito(request.POST)
    if form.is_valid():
            try:
                form.save()
                messages.success(request,"Se ha agregador al carrito")
                return render(request, 'tienda/producto_detalle.html',{'producto': producto, 'form': form})
            except:
                pass
                return redirect('productos')

class CarritoView(generic.TemplateView):
    template_name = 'tienda/carrito.html'

   
#    def get_context_data(self, *args, **kwargs):
#        context = super(CarritoView, self).get_context_data(**kwargs)
#        context["order"] = get_or_set_order_session(self.request)
#        return context