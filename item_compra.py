class ItemCompra:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.cantidad * self.libro.precio

