# CONVERSOR NUMERO A DÍA DE LA SEMANA
def conversor(numero): # creo la función
    if numero not in range (1,8): # si el número no está entre 1 y 7
        return "Tienes que poner un valor entre 1 y 7" # le pido al usuario que escriba un valor correcto
    return semana[numero-1] # de lo contrario devuelvo la posición numero-1 de la lista de días
                            # si devolviese semana[n], el lunes nunca saldría, porque su índice es 0

#PIRÁMIDE INVERTIDA
def piramide_invertida(f): # creo la función
    for i in range (f, 0, -1): # itero entre 0 y el número de filas dado por el usuario, pero al revés
        fila = "" # cada vez que creo una fila, la empiezo con un string vacío
        for j in range(i, 0, -1): # itero entre 0 y el número de filas, pero al revés
            fila += str(j) + " " # añado los elementos de la fila en orden descendente
        print(fila) # imprimo cada fila en orden descendente

# COMPARADOR DE NÚMEROS
def comparacion(num1, num2): # creo la función
    if num1 == num2: # comparo si son iguales
        return "los números son iguales." # devuelvo el resultado de ser iguales
    elif num1 > num2: # comparo si num1 es mayor que num2
        return "el primer número es mayor que el segundo." # devuelvo el resultado de num1 mayor que num2
    else: # en el resto de casos
        return "el segundo número es mayor que el primero." # devuelvo el resultado

# CONTADOR DE LETRAS EN PALABRA
def contador_letras(texto:str, letra:str): # creo la función
    texto = texto.lower() # paso el texto a minúsculas
    conteo = texto.count(letra) # cuento las veces que la letra aparece
    return conteo # devuelvo el número, que ya es un int

# CREAR DICCIONARIO A PARTIR DE UNA PALABRA
import collections # importo la librería collections
def dict_conteo(palabra:str): # creo la función
    solucion = dict(collections.Counter(palabra)) # creo el diccionario gracias al método de la librería collections        
    return solucion # devuelvo el diccionario de la palabra

# AÑADIR/ELIMINAR ELEMENTOS DE UNA LISTA
def añadir_eliminar(lista, comando, elemento = None): # creo la función
    if comando == "add": # si el comando es add
        lista.append(elemento) # añado elemento a la lista
    elif comando == "remove": # si es remove
        if elemento in lista: # en caso de que el elemento exista
            lista.remove(elemento) # elimino el elemento
        
    return lista # devuelvo la lista modificada

# DEVOLVER STRING A PARTIR DE UN CONJUNTO DE PALABRAS INDETERMINADO
def frase(*args:str): # creo la función
    return " ".join(args) # devuelvo los elementos unidos por espacios

# SECUENCIA DE FIBONACCI
def fibonacci(n): # creo la función
    if n <= 1: # si n es 1 o 0
        return n # devuelve n
    else: # en caso contrario
        return fibonacci(n-1) + fibonacci(n-2)

# ÁREAS DE CUADRADO, TRIÁNGULO Y CÍRCULO    
def area_cuadrado(lado): # creo la función
    resultado = lado ** 2
    return resultado # devuelvo el área


def area_triangulo(base, altura):
    resultado = (base * altura) // 2 # calculo el área
    return resultado # devuelvo el área

import math
def area_circulo(radio):
    resultado = math.pi * (radio ** 2) # calculo el área
    return round(resultado) # devuelvo el área

