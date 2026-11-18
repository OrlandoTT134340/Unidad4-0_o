
class jugador:
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__puntaje = 0

    @property
    def Get_nombre(self):       #getter(leer)
        return self.__nombre
    
    def set_nombre(self,mi_nombre):
        self.__nombre = mi_nombre

    def aumentar_puntaje(self,puntos):  
    
        if puntos > 0:
            self.__puntaje += puntos

    def mostrar_estado(self):
          print(f"Nombre: {self.__nombre}, Puntaje: {self.__puntaje}")


    
jugar = jugador("Ana")
jugar.aumentar_puntaje(10)
jugar.aumentar_puntaje(-5)
jugar.mostrar_estado()

