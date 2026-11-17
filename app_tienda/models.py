from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    codigo_pasillo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_pasillo})"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.producto.nombre}"