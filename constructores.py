# se conocen como metodo dunder (double underscore) o metodo magico, se usan para crear objetos a partir de una clase, se ejecuta automaticamente al crear un objeto, se usa para inicializar los atributos de un objeto

# las clases poseen atributos y metodos

class Persona:
  # constructor
  def __init__(self,nombre,apellido):
    self.nombre = nombre
    self.apellido = apellido
  
    
  def mostrar_persona(self):
    print(f"Nombre: {self.nombre} {self.apellido}")
    
    
# creacion objel=tos
if __name__ == "__main__":
  persona1 = Persona("Layla","Acosta")
  persona1.mostrar_persona()
  
  persona2 = Persona("Ian","Sanchez")
  persona2.mostrar_persona()