# Metodos de clase en python - >
class Persona:
  contador_personas = 0
  
  def __init__(self,nombre,apellido):
    Persona.contador_personas += 1
    self._id = Persona.contador_personas
    self._nombre = nombre
    self._apellido = apellido
    
  def mostrar_persona(self):
    print(f"Persona: {self._id} - {self._nombre} {self._apellido}")
    
  @staticmethod
  def get_contador_personas_statico():
    print("Metodo Estatico")
    return Persona.contador_personas  
  # Un metodo estatico es un metodo que pertenece a la clase y no a los objetos de la clase, lo que significa que se puede llamar sin necesidad de crear un objeto de la clase, y no tiene acceso a los atributos de instancia de los objetos, pero si tiene acceso a los atributos de clase, como en este caso el contador_personas, lo que permite obtener el valor del contador de personas sin necesidad de crear un objeto de la clase Persona.
  
  @classmethod
  def get_contador_personas_clase(cls):
    print("Metodo de clase")
    return cls.contador_personas
  # Un metodo de clase es un metodo que pertenece a la clase y no a los objetos
  # esta es la mas recomendada, ya que el primer parametro es cls, que hace referencia a la clase, lo que permite acceder a los atributos de clase de forma mas flexible, ya que si se hereda la clase Persona, el metodo de clase seguira funcionando correctamente, mientras que el metodo estatico no tendria acceso a los atributos de clase de la clase hija, lo que podria generar errores si se intenta acceder a un atributo de clase que no existe en la clase padre pero si en la clase hija.

if __name__ == "__main__":
  print(f"Contador de personas antes de crear objetos: {Persona.contador_personas}")
  
  persona1 = Persona("Juan","Pérez")
  persona1.mostrar_persona()
  
  
  persona2 = Persona("María","Gómez")
  persona2.mostrar_persona()
  
  
  persona3 = Persona("Carlos","López")
  persona3.mostrar_persona()
  
  print(f"Contador de personas después de crear objetos: {Persona.contador_personas}")
  print(f"Contador de personas desde metodo estatico: {Persona.get_contador_personas_statico()}")
  print(f"Contador de personas desde metodo de clase: {Persona.get_contador_personas_clase()}")
  
  # Desde el contexto Dinamico se puede accerder al contexto estatico pero no se puede al reves