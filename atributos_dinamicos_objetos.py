
class Coche:
  def __init__(self,marca,modelo,color):
    self._marca = marca
    self._modelo = modelo 
    self._color = color 
    
  def conducir(self):
    print(f'''
          Conduciendo el coche:
          Marca: {self._marca}
          Modelo: {self._modelo}
          Color: {self._color}
          ''')
    

  @property
  def marca(self):
    return self._marca

  @marca.setter
  def marca(self,marca):
    self._marca = marca
  
  @property
  def modelo(self):
    return self._modelo
  
  @modelo.setter
  def modelo(self,modelo):
    self._modelo = modelo
    
  @property  
  def color(self):
    return self._color
  
  @color.setter
  def color(self,color):
    self._color = color


# Programa principal
if __name__ == "__main__":
  coche1 = Coche("Toyota","Corolla","Rojo")
  coche1.conducir()

  coche1.marca = "Honda"
  coche1.modelo = "Civic"
  coche1.color = "Azul"
  coche1.conducir()
  
  print(f"Atributo marca:{coche1.marca}")
  # intentar agregar un nuevo atributo dinamico al objeto coche1
  setattr(coche1,"nuevo_atributo","Valor del nuevo atributo")
  coche1.nuevo_atributo2 ="Nuevo atributo 2"
  # Se pueden agregar atributos nuevos a un objeto de forma dinamica, incluso si no estan definidos en la clase, pero solo para ese objeto en particular
  print(f"Nuevo atributo: {coche1.nuevo_atributo}")
  coche2 = Coche("Chevrolet","Camaro","Amarillo")
  print(f"Atributos de coche1: {coche1.__dict__}")
  # __dict__ es un atributo especial que contiene un diccionario con los atributos del objeto y sus valores
  print(f"Atributos de coche2: {coche2.__dict__}")