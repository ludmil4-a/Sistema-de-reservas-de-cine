from cine import Cine
from datos import peliculas
from estadisticas import Estadisticas

cine = Cine(peliculas)

while True:

    print("\n===== CINE =====")
    print("1. Reservar entradas")
    print("2. Ver estadísticas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cine.reservar()

    elif opcion == "2":

        print("\n----- Estadísticas -----")

        print(
            "Película más elegida:",
            Estadisticas.pelicula_mas_vista(peliculas).nombre
        )

        print(
            "Horario con mayor demanda:",
            Estadisticas.horario_mas_demandado(peliculas)
        )

        print(
            "Total de entradas vendidas:",
            Estadisticas.total_entradas(peliculas)
        )

    elif opcion == "3":
        print("Hasta luego.")
        break

    else:
        print("Opción incorrecta.")