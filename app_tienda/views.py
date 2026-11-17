from django.shortcuts import redirect, render
from .forms import CategoriaForm, ProductoForm, VentaForm
from .models import Categoria, Producto, Venta


def index(request):
  if request.method == 'POST':
    if 'form_categoria' in request.POST:
      form = CategoriaForm(request.POST)
    elif 'form_producto' in request.POST:
      form = ProductoForm(request.POST)
    elif 'form_venta' in request.POST:
      form = VentaForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('index')

  return render(
      request,
      'app_tienda/index.html',
      {
          'categorias': Categoria.objects.all(),
          'productos': Producto.objects.all(),
          'ventas': Venta.objects.all(),
          'cat_form': CategoriaForm(),
          'prod_form': ProductoForm(),
          'vent_form': VentaForm(),
      },
  )