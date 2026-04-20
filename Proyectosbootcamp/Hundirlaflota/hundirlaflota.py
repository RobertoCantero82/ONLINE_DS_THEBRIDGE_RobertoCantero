'''
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
    
'''
import utils

mi_tablero = utils.crear_tablero() # Llamo a la función y la guardo como variable

print("--- TEST DE TABLERO ---") 
print(mi_tablero) # Imprimo el tablero

print(f"Dimensiones: {mi_tablero.shape}") # Compruebo nº de filas y columnas