from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_descuento(self, porcentaje):
        """Calcula el precio con descuento."""
        return self.precio - (self.precio * (porcentaje / 100))

    def __str__(self):
        return self.nombre