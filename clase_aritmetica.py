class Aritmetica:
  def __init__(self,operando1 = None,operando2 = None):#constructor con parametros opcionales, si no se pasan los parametros al crear el objeto, se asigna el valor None a los atributos, lo que permite crear objetos sin necesidad de pasar argumentos, y luego asignarles valores posteriormente
    self.operando1 = operando1
    self.operando2 = operando2
  
  # No existe el concepto de sobrecarga pero si hay una forma de simularla, utilizando parametros opcionales en el constructor, lo que permite crear objetos con diferentes cantidades de argumentos, y luego asignarles valores posteriormente, como se muestra en el ejemplo de aritmetica3, donde se crea un objeto sin pasar argumentos, y luego se asignan valores a los atributos operando1 y operando2.
  
  # def __init__(self,operando1):
  #   self.operando1 = operando1
  # Python solo toma un constructor por clase, si se define otro constructor, el anterior se sobreescribe, por lo que solo se ejecuta el ultimo constructor definido
   
  def sumar(self,operando1,operando2):
    return operando1 + operando2
  
  def restar(self,operando1,operando2):
    return operando1 - operando2
  
  def multiplicar(self,operando1,operando2):
    return operando1 * operando2
  
  def dividir(self,operando1,operando2):
    return operando1 / operando2
  
if __name__ == "__main__":
  print("Calculadora Aritmetica")
  aritmetica1 = Aritmetica(5,7)
  print(f"Suma: {aritmetica1.sumar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"Resta: {aritmetica1.restar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"Multiplicación: {aritmetica1.multiplicar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"División: {aritmetica1.dividir(aritmetica1.operando1,aritmetica1.operando2)}")

  aritmetica2 = Aritmetica(12,16)
  print("-"*20)
  print(f"Suma: {aritmetica2.sumar(aritmetica2.operando1,aritmetica2.operando2)}")
  print(f"Resta: {aritmetica2.restar(aritmetica2.operando1,aritmetica2.operando2)}")
  print(f"Multiplicación: {aritmetica2.multiplicar(aritmetica2.operando1,aritmetica2.operando2)}")
  print(f"División: {aritmetica2.dividir(aritmetica2.operando1,aritmetica2.operando2)}")
  
  aritmetica3 = Aritmetica()#crea un objeto sin pasar argumentos, los atributos operando1 y operando2 se inicializan con el valor None
  aritmetica3.operando1 = 20#asigna un valor al atributo
  aritmetica3.operando2 = 4
  print("-"*20)
  print(f"Suma: {aritmetica3.sumar(aritmetica3.operando1,aritmetica3.operando2)}")