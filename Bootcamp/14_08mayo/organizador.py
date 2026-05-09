import os
import shutil # esta librería sirve para operaciones con archivos y carpetas a nivel de sistema
import time

print("Iniciando script...")
time.sleep(1)

# importo tuplas con los tipos de extensiones

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')

# creo la primera función, que recibirá una extensión y devolverá la carpeta donde tiene que ir el archivo

def categorizar(extension):
    if extension in doc_types: # si la extensión coincide con la que aparece en la tupla Documentos, devuelve ese string
        return "Documentos"
    elif extension in img_types: # si la extensión coincide con la que aparece en la tupla Imagenes, devuelve ese string
        return "Imagenes"
    elif extension in software_types: # si la extensión coincide con la que aparece en la tupla Software, devuelve ese string
        return "Software"
    else:
        return "Otros" # en caso contrario, devuelve Otros
    
    # creo la función para crear carpetas

def crear_carpeta(ruta):

    carpetas = ["Documentos", "Imagenes", "Software", "Otros"] # creo una lista con los nombres obtenidos para las carpetas

    for carpeta in carpetas: # itera cada elemento de la lista carpetas
        os.makedirs(os.path.join(ruta, carpeta), exist_ok=True) # une la ruta con el nombre de la carpeta y la crea si no existe

# esta sería la función que mueve archivos a su carpeta correspondiente

def organizacion(ruta):

    crear_carpeta(ruta) # crea la carpeta si no existe

    for archivo in os.listdir(ruta): # itera todo lo que hay en la ruta (la carpeta que he indicado)
        ruta_archivo = os.path.join(ruta, archivo) # obtengo la ruta completa de cada archivo
        if os.path.isdir(ruta_archivo): # si es una carpeta, la salto y paso al siguiente elemento
            continue

        extension = os.path.splitext(archivo)[1].lower() # extrae la extensión en minúsculas

        categoria = categorizar(extension) # obtengo la carpeta de destino del archivo

        destino = os.path.join(ruta, categoria, archivo) # construyo la ruta de destino con la carpeta correspondiente

        shutil.move(ruta_archivo, destino) # mueve el archivo a la carpeta que le corresponde

        print(f"Movido: {archivo} -> {categoria}/") # imprime el mensaje

        time.sleep(1) # pausa para ver el progreso en terminal

# por último, se creo la función principal que llevará a cabo todas las operaciones de manera automática

def main(): 
    ruta = r"C:\Users\rober\Desktop\archivosboot" # esta es la ruta que se quiere organizar
    print(f"Organizando archivos en {ruta}") # mensaje de la ruta en la que empiezo  a organizar
    organizacion(ruta) # muevo los archivos
    print("¡Archivos organizados!") # mensaje de confirmación

if __name__ == '__main__': # se este archivo se ejecuta directamente, llama a la función main() y comienza el proceso
    main()