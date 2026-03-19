# Las modificaciones se ven reflejadas en cualquier objeto de la clase, ya que el atributo es compartido por todos los objetos de la clase, a diferencia de los atributos de instancia, que son únicos para cada objeto. En este caso, el atributo clase es un contador que se incrementa cada vez que se crea un nuevo objeto de la clase, y su valor se muestra al crear cada objeto, lo que demuestra que el atributo clase es compartido por todos los objetos de la clase.

class Persona:
  
  atributo_clase = 0
  # se define fuera de cualquier metodo, y se asigna un valor inicial, en este caso 0, lo que indica que no se han creado objetos de la clase aun, y cada vez que se crea un nuevo objeto, se incrementa el valor del atributo clase en 1, lo que permite llevar un conteo de cuantos objetos se han creado de la clase.
  def __init__(self,atributo_instancia):
    self.atributo_instancia = atributo_instancia

if __name__ == "__main__":
  print(f"Valor del atributo clase antes de crear objetos: {Persona.atributo_clase}")
  
  Persona.atributo_clase = 10
  print(f"Valor del atributo clase modificado: {Persona.atributo_clase}")
  
  persona1 = Persona(15)
  print(f"Valor del atributo clase desde persona1: {persona1.atributo_clase}")
  print(f"Valor del atributo instancia de persona1: {persona1.atributo_instancia}")
  
  # creamos segundo objeto
  
  persona2 = Persona(30)
  print(f"Valor del atributo clase desde persona2: {persona2.atributo_clase}")
  print(f"Valor del atributo instancia de persona2: {persona2.atributo_instancia}")
  