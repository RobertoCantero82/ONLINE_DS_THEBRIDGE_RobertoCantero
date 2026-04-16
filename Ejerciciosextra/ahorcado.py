# Quiero crear un juego del ahorcado
# ¿Qué es lo que hay que hacer? ¿Cuáles son los pasos?
# Crear una lista de palabras y elegir una aleatoria
# Para hacerlo más sencillo, que la palabra no tenga más de 5 letras
# Habrá 3 vidas, es decir, el bucle tendrá la condición de que mientras las vidas sean > 3, 
# seguirá funcionando
# Claro, hace falta un input del usuario pero también una palabra a 
# adivinar. ¿Cómo se hace esto último?

# A mitad me he dado cuenta de que hay que utilizar esta librería
import random

# Crear una lista con las palabras a adivinar y elegir una al azar

conjunto_palabras = ["amigo", "coche", "juego", "cosas", "usado", "fuego", "grupo"]
palabra = random.choice(conjunto_palabras)

# Creo las variables fundamentales en el juego (nº de vidas y las letras que se han adivinado ya)

vidas = 3 # empiezo con 3 vidas
letras_adivinadas = [] # voy guardando en una lista las letras que he acertado

# Creo el bucle del juego (el lío gordo)


while vidas > 0: # mientras las vidas sean mayores de cero
    progreso = "" # lo primero que hago es crear una variable string vacía
    for i in palabra: #ahora iteramos sobre la palabra a adivinar 
        if i in letras_adivinadas: # si la letra aparece en la palabra
            progreso += i + " " # la añado a progreso
        else:
            progreso += "_ " # de lo contrario pongo _

    print(f"\nPalabra: {progreso}") # imprimo lo que tengo hasta ahora
    print(f"Vidas restantes: {vidas}") # imprimo las vidas que me quedan

    if "_" not in progreso: # si en la palabra progreso no hay _
        print("¡Felicidades! Has ganado.") # imprimo la felicitación
        break # paro el programa, porque el usuario ha ganado   

    intento = input("Dime una letra: ").lower() # pido otra letra

    if intento in palabra: # itero con la nueva letra
        if intento not in letras_adivinadas: # si la nueva letra no la he dicho
            letras_adivinadas.append(intento) # añadela a los intentos
            print(f"¡Bien hecho! La letra '{intento}' está en la palabra.") # imprime 
        else:
            print("Ya habías dicho esa letra.") # dime que ya la había dicho
    else:
        vidas -= 1 # quita una vida
        print(f"Lo siento, la '{intento}' no está.") # imprime el mensaje de fallo

# ¿Qué pasa si el while deja de funcionar? Que el usuario ha perdido, con lo que solo queda
# comprobar que las vidas son cero e imprimir el mensaje de game over.

if vidas == 0: # cuando las vidas llegan a cero
    print(f"\n¡Game Over! Te has quedado sin vidas. La palabra era: {palabra}") # mensaje de fin de juego


