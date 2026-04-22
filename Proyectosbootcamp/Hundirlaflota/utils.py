# IMPORTO LAS LIBRERÍAS NECESARIAS

import random # librería para los barcos aleatorios y los disparos aleatorios
import clases # librería con las clases de barcos
import numpy as np # librería para gestionar matrices y arrays

# FUNCIÓN PARA CREAR TABLEROS DE 3X3 CON " " EN CADA CASILLA

def crear_tablero(tamaño:tuple = (10,10)): 
   tablero = np.full(tamaño, " ") # creo un array de tamaño por defecto 10x10
   return tablero # devuelvo el tablero

# FUNCIÓN PARA MOSTRAR LOS TABLEROS EN TERMINAL

def mostrar_tableros(mi_tablero, tablero_rival): 
   print() # espacio
   print("Mi tablero") # nombre del tablero del jugador
   print(mi_tablero) # imprimo el tablero del jugador
   print() # espacio
   print("Tablero del rival") # nombre del tablero del ordenador
   print(tablero_rival) # imprimo el tablero del ordenador
   print() # espacio

# FUNCIÓN PARA COLOCAR LOS BARCOS EN MI TABLERO
    
def colocar_barcos(mi_tablero): 

   esloras = [2, 2, 2, 3, 3, 4] # creo la lista de esloras
   flota = [] # creo una lista vacía para guardar las posiciones de los barcos que se van creando 

   print("Comienza a desplegar tus barcos:") # imprimo el mensaje para empezar a colocar los barcos

   for i in esloras: # itero por los elementos en la lista de esloras
      barco = clases.Barco(i) # creo el barco de i de eslora
      print(f"Colocando el {barco.nombre} ({i} de eslora)") # imprimo el mensaje del tipo de barco y la longitud de eslora

      while len(barco.coordenadas) < i: # ahora entro en el bucle principal, que se ejecutará mientras la longitud del barco sea menor que la eslora indicada
         # Lo hago a través de try/except, para evitar que los valores no numéricos rompan el juego
         try: # el código principal del bucle empieza a partir de aquí
            print(f"Introduce la casilla {len(barco.coordenadas) + 1} de {i}") # imprimo el mensaje para pedir coordenadas
            f = int(input("Fila (de 0 a 9): ")) # pido el numero de fila
            c = int(input("Columna (de 0 a 9): ")) # pido el número de columna

            if 0 <= f <= 9 and 0 <= c <= 9 and mi_tablero[f,c] == " ": # Si las coordenadas son correctas y en mi tablero hay espacio vacío
               mi_tablero[f,c] = "O" # añado el símbolo del barco a las coordenadas facilitadas
               barco.coordenadas.append((f,c)) # además, añado la posición del barco a su atributo de coordenadas
               print(mi_tablero) # imprimo el tablero del jugador
            else:
               print(f"Casilla no válida. Inténtalo otra vez") # si las coordenadas no son correctas, se piden de nuevo
         except ValueError:
            print(f"Solo se pueden introducir números") # cuando hay error de valor, se imprime el error para guiar al jugador

      flota.append(barco) # por cada iteración correcta voy añadiendo las coordenadas a la lista flota, que guarda las posiciones en el tablero
      
   return flota # devuelvo esa lista para poder operar en los disparos

# FUNCIÓN PARA COLOCAR LOS BARCOS ALEATORIOS DEL RIVAL

def colocar_barcos_rival(tablero_rival):
   esloras = [2, 2, 2, 3, 3, 4] # creo la lista de esloras
   flota_rival = []  # creo una lista vacía para guardar las posiciones de los barcos del ordenador

   for i in esloras: # itero por los elementos en la lista de esloras
      barco = clases.Barco(i) # creo el barco de i de eslora
      colocado = False # por defecto el barco se inicia como no colocado
   
      while not colocado: # entramos en el bucle principal, que se repetirá hasta que tenga el barco aleatorio colocado
         f = np.random.randint(0,10) # obtengo una fila aleatoria entre 0 y 9
         c = np.random.randint(0,10) # obtengo una columna aleatoria entre 0 y 9
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 10:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f+i <= 10:
            provisionales = [(fil, c) for fil in range(f, f+i)]
         
         if provisionales and all(tablero_rival[pos] == " " for pos in provisionales):
            for pos in provisionales:
               tablero_rival[pos] = "O"
               barco.coordenadas.append(pos)
            flota_rival.append(barco)
            colocado = True
   return flota_rival   

# FUNCIÓN PARA DISPARAR
    
def disparar(casilla, tablero, flota):
   f, c = casilla # se piden fila y columna
   if tablero[f,c] == "O": # si las coordenadas apuntan a una casilla con un "O"
      tablero[f,c] = "X" # la convierto a "X"

      for barco in flota: # se itera la lista de barcos puestos por el jugador
         if casilla in barco.coordenadas: # si las coordenadas del disparo coinciden con las del tablero
            barco.recibir_impacto() # se inicia la función de la clase barco de recibir impacto (quita una vida como atributo)

            if barco.hundido(): # si las vidas llegan a cero
               print(f"¡El {barco.nombre} está hundido!") # se imprime hundido
            else:
               print("¡Tocado!") # si quedan vidas, se imprime tocado

      return "tocado" # hay coincidencia de coordenadas
   
   elif tablero[f,c] == " ": # en caso de que se dispare a una casilla en blanco
      tablero[f,c] = "A" # se cambia su valor por una A
      print("¡Agua!") # se imprime el mensaje
      return "agua" # se devuelve agua
   
   else:
      print("Ya habías disparado aquí") # si el disparo se hace a una casilla diferente de "0" o  de " ", es que
                                        # ya se había disparado. Con lo que hay que repetir y se imprime el mensaje
      return "repetido" # devuelve el repetido

   
  


