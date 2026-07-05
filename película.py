class Pelicula:
    def __init__(self, nombre, horario, precio, capacidad):
        self.nombre = nombre
        self.horario = horario
        self.precio = precio
        self.capacidad = capacidad
        self.entradas_vendidas = 0
        self.recaudacion = 0 

    def lugares_disponibles(self):
        return self.capacidad - self.entradas_vendidas

    def vender(self, cantidad):
        if cantidad <= self.lugares_disponibles():
            self.entradas_vendidas += cantidad
            return True
        return False
