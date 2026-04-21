'''
Los archivos que se utilicen para el juego hay que tenerlos en una carpeta aparte, fuera del repositorio del bootcamp.

Habría que pensar en crear un juego más pequeño, para poder hacer la versión de prueba en la presentación.

Primero hay que pensar en los pasos lógicos a seguir para crear el juego.

Elementos que debe tener:
    - Dos tableros que se impriman en pantalla. Uno para poner mis barcos (donde se verá el juego del ordenador)
      y otro para ir adivinando la posición de los barcos del ordenador.
    - Dos tableros, que no se ven, pero que serán del ordenador. Uno incluirá barcos aleatorios y el otro irá 
      registrando mis disparos.
    - Un turno del jugador para colocar sus barcos (3 barcos de 2x1, 2 de 3x1 y 1 de 4x1).
      Aquí se pedirá un input al jugador.
    - Función para disparar
    - Función para saber si he acertado o fallado (también valdrá para el ordenador)
    - Función para que dispare el ordenador
    - Función 
    - Crear un archivo (o varios) de clases para los distintos tipos de barcos
    - De momento tendríamos el archivo principal, uno de funciones y otro de la clase barcos
    
'''
# IMPORTAR LIBRERÍAS

import utils
import numpy as np

# CREAR EL TABLERO E IMPRIMIRLO

mi_tablero = utils.crear_tablero() # Llamo a la función y la guardo como variable

print()
print("        --- TABLERO DEL JUGADOR ---") 
print()
print(mi_tablero) # Imprimo mi tablero
print()
print("        --- TABLERO DE LA MÁQUINA ---") 
print()
print(mi_tablero) # Imprimo el tablero del rival

barcos_jugador = [[(0,1), (0,2)], [(3,4), (4,4), (5,4)]] # creo dos barcos

tablero_jugador_barcos = utils.colocar_barcos(barcos_jugador, mi_tablero) # pongo los barcos en el tablero
print()
print("        --- TABLERO CON BARCOS ---")
print()
print(tablero_jugador_barcos) # imprimo el tablero con los dos barcos