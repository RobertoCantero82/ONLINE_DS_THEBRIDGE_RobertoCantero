# Quiero crear un juego del ahorcado
# ¿Qué es lo que hay que hacer? ¿Cuáles son los pasos?
# Pedir al usuario una letra
# Para hacerlo más sencillo, que la palabra no tenga más de 5 letras
# Habrá 3 vidas, es decir, el bucle irá quitando vidas si el caracter no está
# en la palabra a adivinar
# Claro, hace falta un input del usuario pero también una palabra a 
# adivinar. ¿Cómo se hace esto último?

# Pedir al usuario una letra
palabra = input("¡Bienvenido al ahorcado! Adivina la palabra de 5 letras que estoy pensando. Dime una letra: ")

# Crear la función para que salga una palabra aleatorio a adivinar
def palabra_aleatoria():
    palabra = ""
    return palabra

# 

# Comprobar con un bucle si la letra introducida está en la palabra
# Si se falla, una vida menos
# Si se acierta, las vidas se mantienen igual y se imprime la posicion de la letra junto con _.
# Por ejemplo, si la palabra es camas y se acierta la letra m, se devolvería _ _ m _ _.
# También hay que imprimir, se acierte o se falle, el número de vidas restantes.
vidas = 3
for letra in palabra:
    if letra in palabra:
        vidas = vidas
        print(f"Has acertado. Te quedan {vidas} vidas.")
    else:
        vidas = vidas - 1
        print(f"Has fallado. Te quedan {vidas} vidas.")


