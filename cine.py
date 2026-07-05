from reserva import Reserva

class Cine:

    def __init__(self, peliculas):
        self.peliculas = peliculas

    def mostrar_peliculas(self):
        print("\n===== CARTELERA =====\n")

        for i, p in enumerate(self.peliculas, start=1):
            print(f"{i}. {p.nombre}")
            print(f"   Horario: {p.horario}")
            print(f"   Entradas disponibles: {p.lugares_disponibles()}\n")

    def reservar(self):

        self.mostrar_peliculas()

        opcion = int(input("Seleccione una película: ")) - 1

        pelicula = self.peliculas[opcion]

        cantidad = int(input("Cantidad de entradas: "))

        if pelicula.vender(cantidad):

            print("\nSeleccione el medio de pago")
            print("1 - Efectivo (5% de descuento)")
            print("2 - Tarjeta de Débito (10% de descuento)")
            print("3 - Tarjeta de Crédito (15% de descuento)")
            print("4 - Mercado Pago (20% de descuento)")

            medio = int(input("Opción: "))

            reserva = Reserva(pelicula, cantidad, medio)

            print("\nReserva realizada correctamente.")
            print(f"Importe a pagar: ${reserva.calcular_total():,.2f}")

        else:
            print("\nNo hay capacidad suficiente.")
