'''
EN CLASE:
1. Crea la función `crear_tablero(tamaño)`, un tablero por defecto de 10x10 relleno 
   del carácter "_" con numpy.
2. Crea la función `colocar_barco(barco, tablero)`, que recibirá la lista de casillas 
   de un barco y el tablero donde colocarlo. Prueba primero a posicionar un par de barcos 
   por ejemplo en [(0,1), (1,1)] y [(1,3), (1,4), (1,5), (1,6)]. Los barcos serán Os mayúsculas. 
   Como ves, un barco de dos posiciones de eslora y otro de cuatro.
3. Crea la función `disparar(casilla, tablero)`, si el disparo acierta en un barco 
   sustituye la O por una X (tocado), si es agua, sustituye la _ por una A (Agua). 
   Prueba primero a disparar el barco de 2 casillas.
4. Crea la función `crear_barco(eslora)`, que deberá crear una lista de casillas de un 
   barco en función a la eslora, de forma aleatoria.

INDIVIDUAL:
5. Crea la función `barcos_aleatorios(tablero)`, que deberá de colocar la lista de barcos 
   generados de forma aleatoria (6 barcos en total (3 barcos de eslora 2, 2 de eslora 3 y 1 eslora 4)) 
   ¡Mucho ojo con barcos que estén superpuestos (no pueden ocupar dos barcos la misma casilla) o barcos 
   que se salgan del tablero!
6. Escribe el flujo completo del programa, con la dinámica de turnos y funcionalidades 
   necesarios para jugar contra la máquina (dispara a tu tablero de forma aleatoria). Crea todas las 
   funciones que necesites y aplica todo lo aprendido que te sea útil.
7. Encapsula todo en un `main.py` y un `utils.py` para ejecutarlo desde terminal.
8. Sube tu proyecto a un repositorio de github y prepara una demo (solo se podrá enseñar 
   desde terminal) para la presentación de tu proyecto.
'''

import numpy as np

def crear_tablero(tamaño:tuple = (10,10)):
   '''
   Un tablero por defecto de 10x10 relleno del carácter " " con numpy
   '''
   tablero_jugador = np.full(tamaño, " ")
   return tablero_jugador
    
def colocar_barco(barco, tablero):
   '''
   Recibirá la lista de casillas de un barco y el tablero donde colocarlo. Prueba primero a posicionar un par de 
   barcos por ejemplo en [(0,1), (1,1)] y [(1,3), (1,4), (1,5), (1,6)]. Los barcos serán Os mayúsculas. 
   Como ves, un barco de dos posiciones de eslora y otro de cuatro.
   '''
   lista_barcos


    
def disparar(casilla, tablero):
   '''
   Si el disparo acierta en un barco sustituye la O por una X (tocado), si es agua, sustituye la _ por una A (Agua). 
   Prueba primero a disparar el barco de 2 casillas.
   '''
    
def crear_barco(eslora):
   '''
   Deberá crear una lista de casillas de un barco en función a la eslora, de forma aleatoria.
   '''
    
def barcos_aleatorios():
   '''
   Deberá de colocar la lista de barcos generados de forma aleatoria (6 barcos en total (3 barcos de eslora 2, 
   2 de eslora 3 y 1 eslora 4)) ¡Mucho ojo con barcos que estén superpuestos (no pueden ocupar dos barcos 
   la misma casilla) o barcos que se salgan del tablero!
   '''
    
