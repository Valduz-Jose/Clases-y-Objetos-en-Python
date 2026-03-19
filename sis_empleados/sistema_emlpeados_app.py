from empresa import Empresa
from empleado import Empleado

print("Sistema de empleados")

empresa1 = Empresa("Empresa 1")
empresa1.contratar_empleado("Juan", "Ventas")
empresa1.contratar_empleado("María", "Marketing")
empresa1.contratar_empleado("Pedro", "Marketing")
empresa1.contratar_empleado("Junior", "Ventas")

print(f"Total de empleados: {Empleado.obtener_total_empleados()}")

print(f"Número de empleados en Ventas: {empresa1.obtener_numero_empleados_por_departamento('Ventas')}")

print(f"Número de empleados en Marketing: {empresa1.obtener_numero_empleados_por_departamento('Marketing')}")

empresa1.obtener_total_empleados()