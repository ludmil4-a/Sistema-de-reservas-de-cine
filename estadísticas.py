class Estadisticas:

    @staticmethod
    def pelicula_mas_vista(peliculas):
        return max(peliculas, key=lambda p: p.entradas_vendidas)

    @staticmethod
    def horario_mas_demandado(peliculas):
        return max(peliculas, key=lambda p: p.entradas_vendidas).horario

    @staticmethod
    def total_entradas(peliculas):
        return sum(p.entradas_vendidas for p in peliculas)
