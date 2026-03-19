
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
    
  # def get_marca(self):
  #   return self._marca
  @property
  def marca(self):
    return self._marca
  # Esta es la forma ma pythonica de crear un getter y setter, usando decoradores
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