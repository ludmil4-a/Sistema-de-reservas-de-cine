from cine import Cine
from datos import peliculas

cine = Cine(peliculas)

while True:

    print("\n===== SISTEMA CINE =====")
    print("1. Reservar entradas")
    print("2. Ver ventas por función")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        cine.reservar()

    elif opcion == "2":
        cine.total_ventas_funcion()

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción incorrecta.")
