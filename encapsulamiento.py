# Encapsulamiento, nos permite ocultar la info que almacena un objeto y solo mostrar lo que queremos mostrar, para esto se utilizan los modificadores de acceso
# Se hace uso de los setters y getters para acceder a los atributos privados de una clase

class Coche:
  def __init__(self,marca,modelo,color):
    self.marca = marca #atributo publico
    self._modelo = modelo #atributo protegido (no se deberia acceder directamente)
    self.__color = color #atributo privado (no se puede acceder directamente)
  def conducir(self):
    print(f'''
          Conduciendo el coche:
          Marca: {self.marca}
          Modelo: {self._modelo}
          Color: {self.__color}
          ''')
    
# Programa principal
if __name__ == "__main__":
  coche1 = Coche("Toyota","Corolla","Rojo")
  coche1.conducir()
  #No se deberia acceder a los atributos que no son publicos
  coche1.marca = "Honda" #se puede modificar el atributo publico
  coche1._modelo = "Civic" #se puede modificar el atributo protegido pero no es recomendable
  coche1.__color = "Azul" #no se puede modificar el atributo privado, genera un error
  coche1._Coche__color = "Azul" #se puede modificar el atributo privado utilizando el nombre de la clase, pero no se deberia hacer esto
  coche1.conducir()