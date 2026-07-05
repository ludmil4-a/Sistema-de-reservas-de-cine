from reserva import Reserva

class Cine:

    def __init__(self, peliculas):
        self.peliculas = peliculas

    def mostrar_peliculas(self):

        print("\n===== CARTELERA =====\n")

        for i, p in enumerate(self.peliculas, start=1):
            print(f"{i}. {p.nombre}")
            print(f"   Horario: {p.horario}")
            print(f"   Precio: ${p.precio}")
            print(f"   Disponibles: {p.lugares_disponibles()}\n")

    def reservar(self):

        self.mostrar_peliculas()

        try:
            opcion = int(input("Seleccione una película: ")) - 1

            if opcion < 0 or opcion >= len(self.peliculas):
                print("\n Error: Película inexistente")
                return

            pelicula = self.peliculas[opcion]

            cantidad = int(input("Cantidad de entradas: "))

            if cantidad <= 0:
                print("\n Error: cantidad inválida")
                return

            if cantidad > pelicula.lugares_disponibles():
                print("\n Error: entradas agotadas")
                return

            if not pelicula.vender(cantidad):
                print("\n No se pudo realizar la venta")
                return

            print("\nSeleccione el medio de pago")
            print("1 - Efectivo (5%)")
            print("2 - Débito (10%)")
            print("3 - Crédito (15%)")
            print("4 - Mercado Pago (20%)")

            medio = int(input("Opción: "))

            if medio not in [1, 2, 3, 4]:
                print("\n Error: medio de pago inválido")
                return

            reserva = Reserva(pelicula, cantidad, medio)

            total = reserva.calcular_total()
            asientos = reserva.generar_asientos()

            print("\n===== RESUMEN =====")
            print(f"Película: {pelicula.nombre}")
            print(f"Asientos: {asientos}")
            print(f"Total a pagar: ${total:,.2f}")

        except ValueError:
            print("\n Error: Debe ingresar números válidos")

    def total_ventas_funcion(self):

        print("\n===== VENTAS POR FUNCIÓN =====\n")

        for p in self.peliculas:
            total = p.entradas_vendidas * p.precio

            print(f"{p.nombre} - {p.horario}")
            print(f"Vendidas: {p.entradas_vendidas}")
            print(f"Recaudación: ${total:,.2f}\n")
