class Aritmetica:
  def __init__(self,operando1,operando2):
    self.operando1 = operando1
    self.operando2 = operando2
  
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