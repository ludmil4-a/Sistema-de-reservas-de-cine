class Reserva:
    PRECIO = 3000

    def __init__(self, pelicula, cantidad, promo=False):
        self.pelicula = pelicula
        self.cantidad = cantidad
        self.promo = promo
