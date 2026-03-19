class Persona:
  contador_personas = 0
  
  def __init__(self,nombre,apellido):
    Persona.contador_personas += 1
    self._id = Persona.contador_personas
    self._nombre = nombre
    self._apellido = apellido
    # Incrementamos en 1 el contador de personas cada vez que se crea un nuevo objeto de la clase Persona, lo que nos permite llevar un conteo de cuantas personas se han creado.
    
  def mostrar_persona(self):
    print(f"Persona: {self._id} - {self._nombre} {self._apellido}")
    
if __name__ == "__main__":
  print(f"Contador de personas antes de crear objetos: {Persona.contador_personas}")
  
  persona1 = Persona("Juan","Pérez")
  persona1.mostrar_persona()
  
  
  persona2 = Persona("María","Gómez")
  persona2.mostrar_persona()
  
  
  persona3 = Persona("Carlos","López")
  persona3.mostrar_persona()
  
  print(f"Contador de personas después de crear objetos: {Persona.contador_personas}")