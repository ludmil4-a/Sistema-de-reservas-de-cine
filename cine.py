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

        try:
            self.mostrar_peliculas()

            opcion = int(input("Seleccione una película: ")) - 1

            if opcion < 0 or opcion >= len(self.peliculas):
                print("\nPelícula inválida")
                return

            pelicula = self.peliculas[opcion]

            cantidad = int(input("Cantidad de entradas: "))

            if cantidad <= 0:
                print("\n Error: debe comprar al menos 1 entrada")
                return

            if cantidad > pelicula.lugares_disponibles():
                print("\n Entradas agotadas")
                return

            pelicula.vender(cantidad)

            print("\nSeleccione el medio de pago")
            print("1 - Efectivo (20%)")
            print("2 - Débito (15%)")
            print("3 - Crédito (10%)")
            print("4 - Mercado Pago (5%)")

            medio = int(input("Opción: "))

            if medio not in [1, 2, 3, 4]:
                print("\n Medio de pago inválido")
                return

            reserva = Reserva(pelicula, cantidad, medio)

            total = reserva.calcular_total()
            asientos = reserva.generar_asientos()

            # 💰 ACUMULAMOS RECAUDACIÓN REAL
            pelicula.recaudacion += total

            print("\n===== RESUMEN DE COMPRA =====")
            print(f"Película: {pelicula.nombre}")
            print(f"Asientos: {asientos}")
            print(f"Total a pagar: ${total:,.2f}")

        except ValueError:
            print("\n Error: debe ingresar números válidos")

    def total_ventas_funcion(self):

        print("\n===== VENTAS POR FUNCIÓN =====\n")

        for p in self.peliculas:
            print(f"{p.nombre} - {p.horario}")
            print(f"Entradas vendidas: {p.entradas_vendidas}")
            print(f"Recaudación real: ${p.recaudacion:,.2f}\n")
