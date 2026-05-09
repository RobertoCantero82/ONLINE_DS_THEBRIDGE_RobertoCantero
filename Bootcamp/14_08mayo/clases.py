# importo librerías

import os
import shutil

# creo las tuplas

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py', '.ipynb')

# inicio la clase y sus atributos

class Fichero:

    def __init__(self, ruta):
        self.ruta = ruta # guarda la ruta del archivo
        self.nombre = os.path.basename(ruta) # extrae el nombre 
        self.extension = os.path.splitext(self.nombre)[1].lower() # extrae la extensión
        self.categoria = self.categorizar() # llama a la función categorizar para saber en qué carpeta va

    #devuelve la carpeta de destino según la extensión del archivo
    
    def categorizar(self):
        if self.extension in doc_types:
            return "Documentos"
        elif self.extension in img_types:
            return "Imagenes"
        elif self.extension in software_types:
            return "Software"
        else:
            return "Otros"

# mueve el archivo a la carpeta correspondiente

    def mover(self, ruta_base):
        destino = os.path.join(ruta_base, self.categoria, self.nombre)
        shutil.move(self.ruta, destino)
        print(f"Movido: {self.nombre} -> {self.categoria}/")