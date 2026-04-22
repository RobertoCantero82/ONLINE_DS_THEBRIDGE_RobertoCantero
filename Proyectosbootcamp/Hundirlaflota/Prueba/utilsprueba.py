#IMPORTO LAS LIBRERÍAS

import random # librería para los barcos aleatorios y los disparos aleatorios
import clasesprueba # librería con las clases de barcos
import numpy as np # librería para gestionar matrices y arrays

def crear_tablero(tamaño:tuple = (3,3)): # función para crear tableros de 3x3 con " " en cada casilla
  
   tablero = np.full(tamaño, " ") # creo un array de tamaño por defecto 3x3
   return tablero # devuelvo el tablero

def mostrar_tableros(mi_tablero, tablero_rival): # función para mostrar los tableros en terminal
    print() # espacio
    print("Mi tablero") # nombre del tablero del jugador
    print(mi_tablero) # imprimo el tablero del jugador
    print() # espacio
    print("Tablero del rival") # nombre del tablero del ordenador
    print(tablero_rival) # imprimo el tablero del ordenador
    print() # espacio
    
def colocar_barcos(mi_tablero): # función para colocar los barcos en mi tablero

   esloras = [2] # creo la lista de esloras que se pide en el ejercicio
   flota = [] # creo una lista vacía con 

   print("Comienza a desplegar tus barcos:")

   for i in esloras:
      barco = clasesprueba.Barco(i)
      print(f"Colocando el {barco.nombre} ({i} de eslora)")

      while len(barco.coordenadas) < i:
         try:
            print(f"Introduce la casilla {len(barco.coordenadas) + 1} de {i}")
            f = int(input("Fila (de 0 a 2): "))
            c = int(input("Columna (de 0 a 2): "))

            if 0 <= f <= 2 and 0 <= c <= 2 and mi_tablero[f,c] == " ":
               mi_tablero[f,c] = "O"
               barco.coordenadas.append((f,c))
               print(mi_tablero)
            else:
               print(f"Casilla no válida. Inténtalo otra vez")
         except ValueError:
            print(f"Solo se pueden introducir números")

      flota.append(barco)
      
   return flota
      
    
def disparar(casilla, tablero, flota):
   f, c = casilla
   if tablero[f,c] == "O":
      tablero[f,c] = "X"

      for barco in flota:
         if casilla in barco.coordenadas:
            barco.recibir_impacto()

            if barco.hundido():
               print(f"¡El {barco.nombre} está hundido!")
            else:
               print("¡Tocado!")

      return "tocado"
   
   elif tablero[f,c] == " ":
      tablero[f,c] = "A"
      print("¡Agua!")
      return "agua"
   
   else:
      print("Ya habías disparado aquí")
      return "repetido"

   
  
def colocar_barcos_rival(tablero_rival):
   esloras = [2] 
   flota_rival = []  

   for i in esloras:
      barco = clasesprueba.Barco(i)
      colocado = False
   
      while not colocado:
         f = np.random.randint(0,3)
         c = np.random.randint(0,3)
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 3:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f+i <= 3:
            provisionales = [(fil, c) for fil in range(f, f+i)]
         
         if provisionales and all(tablero_rival[pos] == " " for pos in provisionales):
            for pos in provisionales:
               tablero_rival[pos] = "O"
               barco.coordenadas.append(pos)
            flota_rival.append(barco)
            colocado = True
   return flota_rival   

