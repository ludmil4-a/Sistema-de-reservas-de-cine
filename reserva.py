class Reserva:

    def __init__(self, pelicula, cantidad, medio_pago):
        self.pelicula = pelicula
        self.cantidad = cantidad
        self.medio_pago = medio_pago
        self.descuento = 0
        self.medio = ""

    def calcular_total(self):

        subtotal = self.cantidad * self.pelicula.precio

        if self.medio_pago == 1:
            self.descuento = 0.20
            self.medio = "Efectivo (20%)"

        elif self.medio_pago == 2:
            self.descuento = 0.15
            self.medio = "Débito (15%)"

        elif self.medio_pago == 3:
            self.descuento = 0.10
            self.medio = "Crédito (10%)"

        elif self.medio_pago == 4:
            self.descuento = 0.05
            self.medio = "Mercado Pago (5%)"

        else:
            self.descuento = 0
            self.medio = "Sin descuento"

        total = subtotal - (subtotal * self.descuento)

        print(f"\nMedio de pago: {self.medio}")
        print(f"Descuento aplicado: {self.descuento * 100:.0f}%")

        return total

    def generar_asientos(self):

        inicio = self.pelicula.entradas_vendidas - self.cantidad + 1
        return list(range(inicio, inicio + self.cantidad))
