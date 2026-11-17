from django import forms
from .models import Categoria, Producto, Venta


class CategoriaForm(forms.ModelForm):

  class Meta:
    model = Categoria
    fields = '__all__'


class ProductoForm(forms.ModelForm):

  class Meta:
    model = Producto
    fields = '__all__'


class VentaForm(forms.ModelForm):

  class Meta:
    model = Venta
    fields = '__all__'

    