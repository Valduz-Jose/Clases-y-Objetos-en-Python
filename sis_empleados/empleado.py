# la empresa desea saber el total de empleados y total de empleados de un depa en particular. se deebn crear las clases empleado y empresa en archivos separados y la cracion de objetos en otro archivo

class Empleado:
  contador_empleados = 0
  
  def __init__(self,nombre,departamento):
    self.nombre = nombre
    self.departamento = departamento
    Empleado.contador_empleados += 1
    self.id = Empleado.contador_empleados
    
  @classmethod
  def obtener_total_empleados(cls):
    return cls.contador_empleados