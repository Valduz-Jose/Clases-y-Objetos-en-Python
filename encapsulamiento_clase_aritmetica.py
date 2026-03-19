class Aritmetica:
  def __init__(self,operando1 = None,operando2 = None):
    self._operando1 = operando1
    self._operando2 = operando2
    
  @property
  def operando1(self):
    return self._operando1
  @operando1.setter
  def operando1(self,operando1):
    self._operando1 = operando1
  
  @property
  def operando2(self):
    return self._operando2
  @operando2.setter
  def operando2(self,operando2):
    self._operando2 = operando2
   
  def sumar(self,_operando1,_operando2):
    return _operando1 + _operando2
  
  def restar(self,_operando1,_operando2):
    return _operando1 - _operando2
  
  def multiplicar(self,_operando1,_operando2):
    return _operando1 * _operando2
  
  def dividir(self,_operando1,_operando2):
    return _operando1 / _operando2
  
if __name__ == "__main__":
  print("Calculadora Aritmetica")
  aritmetica1 = Aritmetica(5,7)
  print(f"Suma: {aritmetica1.sumar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"Resta: {aritmetica1.restar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"Multiplicación: {aritmetica1.multiplicar(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"División: {aritmetica1.dividir(aritmetica1.operando1,aritmetica1.operando2)}")
  print(f"Valor Operando1 del objeto aritmetica1: {aritmetica1.operando1}")
  print(f"Valor Operando2 del objeto aritmetica1: {aritmetica1.operando2}")

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
  print(f"División: {aritmetica1.dividir(aritmetica2.operando1,aritmetica2.operando2)}")
  print(f"Valor Operando1 del objeto aritmetica2: {aritmetica2.operando1}")
  print(f"Valor Operando2 del objeto aritmetica2: {aritmetica2.operando2}")