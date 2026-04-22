
# IMPORTAR LIBRERÍAS

import clases
import utils
import random
import numpy as np

# CREAR EL TABLERO E IMPRIMIRLO

mi_tablero = utils.crear_tablero() # Creo mi tablero a partir de una función
tablero_rival = utils.crear_tablero() # Creo el tablero del rival a partir de una función
tablero_rival_oculto = utils.crear_tablero() # Tiene los barcos del rival

print("¡Bienvenido a Hundir la Flota!")
print()

# COLOCAMOS LOS BARCOS

flota = utils.colocar_barcos(mi_tablero)
flota_rival = utils.colocar_barcos_rival(tablero_rival_oculto)

# BUCLE DE JUEGO

print("¡Empieza el juego!")

jugador_gana = False
rival_gana = False

while not jugador_gana and not rival_gana:
    
    print("─" * 30)
    utils.mostrar_tableros(mi_tablero, tablero_rival)

    # Empieza el turno del jugador

    try:
        f = int(input("Dispara la fila (del 0 al 9): "))
        c = int(input("Dispara la columna (del 0 al 9): "))

        disparo = utils.disparar((f,c), tablero_rival_oculto, flota_rival)

        if disparo == "tocado":
          tablero_rival[f,c] = "X"
        elif disparo == "agua":
          tablero_rival[f,c] = "A"
    except ValueError:
       print("Tienes que introducir números del 0 al 9")
       continue


    # Es el turno del rival

    if disparo == "agua" or disparo == "repetido":  # ← añade esta condición de nuevo
        f_aleatoria = np.random.randint(0, 10)       # ← genera las coordenadas primero
        c_aleatoria = np.random.randint(0, 10)
        print(f"El rival dispara a ({f_aleatoria}, {c_aleatoria})")
        disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)

        while disparo_rival == "tocado":
            f_aleatoria = np.random.randint(0, 10)
            c_aleatoria = np.random.randint(0, 10)
            print(f"El rival repite turno y dispara a ({f_aleatoria}, {c_aleatoria})")
            disparo_rival = utils.disparar((f_aleatoria, c_aleatoria), mi_tablero, flota)

    # Compruebo si hay victoria de alguno
    jugador_gana = not np.any(tablero_rival_oculto == "O")
    rival_gana = not np.any(mi_tablero == "O")

# RESULTADO

utils.mostrar_tableros(mi_tablero, tablero_rival)

if jugador_gana:
    print("Has ganado (¬_¬)")
elif rival_gana:
    print("Te he ganado! ¡Muahahahaha! ( ^ㅂ^ )")

