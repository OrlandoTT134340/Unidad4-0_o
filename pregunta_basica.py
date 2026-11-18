
#class pregunta 
class Pregunta:
   def __init__(self, texto, respuesta_correcta):
    print("bandera")
    self.texto = texto
    self.respuesta_correcta = respuesta_correcta
   
   def verificar (self, respuesta_usuario):  
    if respuesta_usuario.lower().strip() == self.respuesta_correcta.lower().strip():
      print("¡Verdadero! Respuesta correcta.\n")
      return True  # Devuelve True si acertó
    else:
      print("Falso. Respuesta incorrecta.\n")
      return False # Devuelve False si falló

Pregunta1 = Pregunta("¿Cual especie de animal es Tai lung?","leopardo")
respuesta_usuario = str(input("¿¿Cual especie de animal es Tai lung?"))
Pregunta1.verificar(respuesta_usuario)
  

 
      
#objetos
