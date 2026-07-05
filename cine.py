from reserva import Reserva

class Cine:

    def __init__(self, peliculas):
        self.peliculas = peliculas

    def mostrar_peliculas(self):
        print("\nCartelera\n")

        for i, p in enumerate(self.peliculas, start=1):
            print(
                f"{i}. {p.nombre} - {p.horario} - "
                f"Disponibles: {p.lugares_disponibles()}"
            )

    def reservar(self):

        self.mostrar_peliculas()

        opcion = int(input("\nSeleccione película: ")) - 1

        pelicula = self.peliculas[opcion]

        cantidad = int(input("Cantidad de entradas: "))

        promo = input("¿Aplicar promoción? (s/n): ").lower() == "s"

        if pelicula.vender(cantidad):

            reserva = Reserva(pelicula, cantidad, promo)

            print("\nReserva realizada correctamente.")
            print(f"Importe: ${reserva.calcular_total():,.0f}")

        else:
            print("\nNo hay capacidad suficiente.")