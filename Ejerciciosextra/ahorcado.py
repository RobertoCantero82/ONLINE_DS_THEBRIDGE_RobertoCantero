import random

# Crear una lista con las palabras a adivinar y elegir una al azar

conjunto_palabras = ["amigo", "coche", "juego", "cosas", "usado", "fuego", "grupo"]
palabra = random.choice(conjunto_palabras)

# Creo las variables fundamentales en el juego (nº de vidas, letras que se han adivinado y letras que se han fallado)

vidas = 6 # empiezo con 6 vidas
letras_adivinadas = [] # voy guardando en una lista las letras que he acertado
letras_falladas = [] # lista con las letras ya dichas y falladas

# Creo el bucle del juego (el lío gordo)


while vidas > 0: # mientras las vidas sean mayores de cero

    progreso = "" # lo primero que hago es crear una variable string vacía

    for i in palabra: #ahora iteramos sobre la palabra aleatoria 
        if i in letras_adivinadas: # si la letra aparece en la palabra
            progreso += i + " " # la añado a progreso
        else:
            progreso += "_ " # de lo contrario pongo _

    print(f"\nPalabra: {progreso}") # imprimo lo que tengo hasta ahora
    print(f"Vidas restantes: {vidas}") # imprimo las vidas que me quedan
    print(f"Letras falladas: {', '.join(letras_falladas)}")

    if "_" not in progreso: # si en la palabra progreso no hay _
        print("¡Felicidades! Has ganado.") # imprimo la felicitación
        break # paro el programa, porque el usuario ha ganado   

    intento = input("Dime una letra: ").lower() # pido otra letra

    if intento in palabra: # si la letra está en la palabra aleatoria
        if intento not in letras_adivinadas: # si la nueva letra no la he dicho
            letras_adivinadas.append(intento) # añadela a los intentos
            print(f"¡Bien hecho! La letra '{intento}' está en la palabra.") # imprime 
        else:
            print("Ya habías dicho esa letra.") # dime que ya la había dicho
    else:
        if intento not in letras_falladas:
            letras_falladas.append(intento) # añado a la lista de letras falladas
            vidas -= 1 # quito una vida
            print(f"Lo siento, la '{intento}' no está.") # imprimo el mensaje
        else:
            print(f"Ya habías fallado con la letra '{intento}'. No te quito más vidas.") # introduzco el caso de que el jugador se despiste
                                                                                         # y meta una letra fallada por segunda vez

# ¿Qué pasa si el while deja de funcionar? Que el usuario ha perdido, con lo que solo queda
# comprobar que las vidas son cero e imprimir el mensaje de game over.

if vidas == 0: # cuando las vidas llegan a cero
    print(f"\n¡Game Over! Te has quedado sin vidas. La palabra era: {palabra}") # mensaje de fin de juego


