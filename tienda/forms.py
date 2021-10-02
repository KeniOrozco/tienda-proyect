from django import forms
from .models import Producto, OrdenItem, Orden


class AgregarAlCarrito(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields = ('cantidad','producto')
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto': forms.NumberInput(attrs={'class': 'form-control'})
        }

