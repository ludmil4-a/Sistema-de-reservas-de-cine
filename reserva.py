class Reserva:
    PRECIO = 3000

    def __init__(self, pelicula, cantidad, promo=False):
        self.pelicula = pelicula
        self.cantidad = cantidad
        self.promo = promo

    def calcular_total(self):
        total = self.cantidad * self.PRECIO

        if self.promo:
            total *= 0.90

        return total
