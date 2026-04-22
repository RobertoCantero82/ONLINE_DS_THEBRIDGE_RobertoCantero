# Aquí crearé las clases de barcos (tanto para el jugador como para el ordenador)

class Barco: # creo la clase Barco
    
    def __init__(self, eslora): # inicio su definición, que necesitará de un tamaño de eslora
        self.eslora = int(eslora) # la eslora debe ser un int
        self.coordenadas = [] # incluyo coordenadas para luego poder situar al barco en el tablero
        self.vidas = eslora # las vidas del barco serán iguales a su eslora
        if self.eslora == 2:
            self.nombre = "Buque" # si la eslora es 2, el nombre será Buque
        elif self.eslora == 3:
            self.nombre = "Acorazado" # si la eslora es 3, el nombre será Acorazado
        elif self.eslora == 4:
            self.nombre = "Destructor" # si la eslora es 4, el nombre será Destructor
        else:
            self.nombre = "Barco" # en cualquier otro caso, Barco
    
    def recibir_impacto(self):
        self.vidas -= 1

    def hundido(self):
        return self.vidas == 0
    
        
