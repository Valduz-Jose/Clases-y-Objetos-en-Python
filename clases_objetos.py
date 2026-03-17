# las clases poseen atributos y metodos

class Persona:
  def inicializar_persona(self,nombre,apellido):
    self.nombre = nombre
    self.apellido = apellido
    
  def mostrar_persona(self):
    print(f"Nombre: {self.nombre} {self.apellido}")
    
    
# creacion objel=tos
if __name__ == "__main__":
  persona1 = Persona()#crea un objeto vacio
  persona1.inicializar_persona("Layla","Acosta")
  persona1.mostrar_persona()
  
  persona2 = Persona()
  persona2.inicializar_persona("Ian","Sanchez")
  persona2.mostrar_persona()