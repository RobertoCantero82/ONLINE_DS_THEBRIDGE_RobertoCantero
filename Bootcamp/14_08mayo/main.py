# importar librerías 

import os
import time
from clases import Fichero

# print inicia con un segundo de delay

print("Iniciando script...")
time.sleep(1)

# función principal para realizar el proceso de organización de archivos

def main():

    ruta = r"C:\Users\rober\Desktop\archivosboot" # ruta de la carpeta que hay que organizar

    print(f"Organizando archivos en {ruta}") # mensaje de inicio de movimientos
    
    carpetas = ["Documentos", "Imagenes", "Software", "Otros"] # lista con las carpetas

    for carpeta in carpetas: # itero entre las carpetas
        os.makedirs(os.path.join(ruta, carpeta), exist_ok=True) # creo la carpeta si no existe
    
    for archivo in os.listdir(ruta): # itero entre los elementos de la ruta
        ruta_archivo = os.path.join(ruta, archivo) # construyo la ruta completa
        if os.path.isdir(ruta_archivo): # si es una carpeta la salta y pasa al siguiente elemento
            continue
        fichero = Fichero(ruta_archivo) # crea el objeto fichero con la ruta
        fichero.mover(ruta) # mueve el objeto a la carpeta correspondiente
        time.sleep(1)

    print("¡Archivos organizados!") # mensaje final
        
if __name__ == '__main__': # se este archivo se ejecuta directamente, llama a la función main() y comienza el proceso 
    main()