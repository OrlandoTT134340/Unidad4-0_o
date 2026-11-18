#Orlando Escobedo Palafox   
#juegooo Pd: extraño new jeans
#15/11/26 

class ElementoJuego:

    def __init__(self,texto ,opciones: list[str],indice_correcto):
        self.texto = texto
        self.opciones = opciones
        self.indice_correcto = indice_correcto

    def mostrar(self):
        print("mostrando elemento")
        print(self.texto)
        for self.indice_correcto, seleccion in enumerate(self.opciones, start=1):
                 print(f"{self.indice_correcto}. {seleccion}")
        
        return pregunta_multiple

    def Estacorrecto (self, respuesta):   
        if respuesta.lower().strip() == "panda rojo" or respuesta.lower().strip() == "1" or respuesta == 1:
          print("¡Verdadero! Respuesta correcta.\n")
          return True  # Devuelve True si acertó
        else:
          print("Falso. Respuesta incorrecta.\n")
          return False # Devuelve False si falló

        
class pregunta_multiple(ElementoJuego):    
    def opcion_lista(self):
     print("El maestro Shifu es un Panda Rojo")
    

opcion = pregunta_multiple("¿Cual especie de animal es el maestro shifu?",["Panda Rojo","leopardo","Tigre","Tortuga"],1)
opcion.mostrar() 
respuesta = input("Ingrese su opcion:")
opcion.Estacorrecto(respuesta)
opcion.opcion_lista()




