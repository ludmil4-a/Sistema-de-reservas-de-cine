## Trabajo Final Integrador - Laboratorio de Python 

<br><br>

## Integrantes del grupo D32:

  * Gómez Feldmann Ludmila Selene.
  * Gonzalez Lionel Asdrubal.
  * Vallejos Priscila Jaquelin.

<br><br>

## Comisión:   K1.4.

<br><br>

## Escenario:

  Sistema de reservas de cine
    El sistema deberá administrar reservas de entradas para funciones de cine. Podrá contemplar selección de películas, horarios disponibles, cantidad de entradas, control de capacidad de salas, promociones y cálculo de importes.
    La solución podrá incorporar estadísticas básicas relacionadas con películas más elegidas, horarios con mayor demanda o cantidad total de entradas vendidas.

<br><br>

## Descripción del sistema:

  El algoritmo diseñado ayuda en la administración de ventas de entradas para funciones del cine. Por pantalla, le muestra al usuario la selección de películas disponibles del día, indicando el horario de proyección; el precio de cada entrada y la disponibilidad de los asientos por sala. En términos de pago, le ofrece distintas opciones, cada una cuenta con un descuento determinado. 
  Por otro lado, a la administración, le brinda la siguiente información: la cantidad de venta de entradas por películas, el horario pico de asistencia del público, las ganancias totales recaudadas y la película con más elegida. 

<br><br>

## Instrucciones de ejecución:

  pelicula.py
  
  * "__init__(self, nombre, horario, precio, capacidad)" : Constructor que inicializa los atributos básicos y los contadores de ventas y recaudación.

  * "lugares_disponibles(self)" : Calcula el espacio restante restando las entradas vendidas a la capacidad total de la sala.  

  * "vender(self, cantidad)" : Verifica si hay cupos suficientes; si es así, actualiza las entradas vendidas y retorna True, de lo contrario retorna False.
  
<br><br>

  reserva.py
  
  * "__init__(self, pelicula, cantidad, medio_pago)" : Inicializa la reserva vinculándola a una película específica, la cantidad y el medio de pago seleccionado.  

  * "calcular_total(self)" : Aplica el descuento correspondiente según el medio de pago (1: 20%, 2: 15%, 3: 10%, 4: 5%) y calcula el importe final.

  * "generar_asientos(self)" : Genera una lista con los números de asiento asignados basándose en las ventas previas.
  

<br><br>

  estadísticas.py
  
  * "pelicula_mas_vista(peliculas)" : Retorna el objeto Pelicula con la mayor cantidad de entradas vendidas.

  * "horario_mas_demandado(peliculas)" : Devuelve el horario de la función que tiene más entradas vendidas.

  * "total_entradas(peliculas)" : Calcula la suma total de entradas vendidas considerando todas las funciones.
  

<br><br>

  datos.py
  
  * "Archivo de configuración que contiene la lista inicial de objetos Pelicula que componen la cartelera".
  

 <br><br>

  Cine.py
  
  * "mostrar_peliculas(self)" : Imprime en consola la cartelera actual con disponibilidad de salas.

  * "reservar(self)" : Gestiona el flujo de selección de película, cantidad, pago y confirmación de compra.

  * "total_ventas_funcion(self)" : Muestra un resumen de ventas y recaudación real por cada película.

 <br><br>

  main.py
  
  * "Punto de entrada de la aplicación. Ejecuta el bucle principal (while True) que muestra el menú al usuario y llama a los métodos de la clase Cine".
  
  <br><br>

## Link del vídeo explicativo:
  https://drive.google.com/file/d/1hLf4t-5xSb2_wsmyi5bFa80hNXMkD9iX/view?usp=drive_link
