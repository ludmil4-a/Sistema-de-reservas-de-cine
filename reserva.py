class Reserva:

    PRECIO = 3000

    def __init__(self, pelicula, cantidad, medio_pago):
        self.pelicula = pelicula
        self.cantidad = cantidad
        self.medio_pago = medio_pago

    def calcular_total(self):

        subtotal = self.cantidad * self.PRECIO

        if self.medio_pago == 1:
            descuento = 0.05
            medio = "Efectivo"

        elif self.medio_pago == 2:
            descuento = 0.10
            medio = "Tarjeta de Débito"

        elif self.medio_pago == 3:
            descuento = 0.15
            medio = "Tarjeta de Crédito"

        elif self.medio_pago == 4:
            descuento = 0.20
            medio = "Mercado Pago"

        else:
            descuento = 0
            medio = "Sin descuento"

        total = subtotal - (subtotal * descuento)

        print(f"\nMedio de pago: {medio}")
        print(f"Descuento aplicado: {descuento * 100:.0f}%")

        return total
