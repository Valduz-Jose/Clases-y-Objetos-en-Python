
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
    
  def get_marca(self):
    return self._marca
  
  def set_marca(self,marca):
    self._marca = marca
    
  def get_modelo(self):
    return self._modelo
  
  def set_modelo(self,modelo):
    self._modelo = modelo
    
  def get_color(self):
    return self._color
  
  def set_color(self,color):
    self._color = color


# Programa principal
if __name__ == "__main__":
  coche1 = Coche("Toyota","Corolla","Rojo")
  coche1.conducir()

  coche1.set_marca("Honda")
  coche1.set_modelo("Civic")
  coche1.set_color("Azul")
  coche1.conducir()