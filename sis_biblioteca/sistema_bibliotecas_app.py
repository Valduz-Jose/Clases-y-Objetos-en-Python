from biblioteca import Biblioteca
from libro import Libro

bibliotecaNacional = Biblioteca("Biblioteca Nacional")
print(f"-"*50)
print(f"Bienvenido a {bibliotecaNacional.nombre}")

# libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Realismo mágico")
libro4 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio")
libro5 = Libro("El código Da Vinci", "Dan Brown", "Thriller")

# agregar libros a la biblioteca
bibliotecaNacional.agregar_libros(libro1)
bibliotecaNacional.agregar_libros(libro2)
bibliotecaNacional.agregar_libros(libro3)
bibliotecaNacional.agregar_libros(libro4)
bibliotecaNacional.agregar_libros(libro5)

# buscar libro por autor

autor = "Gabriel García Márquez"
print(f"-"*50)
print(f"Buscando libros del autor: {autor}")
bibliotecaNacional.buscar_libro_por_autor(autor)

# buscar por genero
print(f"-"*50)
genero = "Realismo mágico"
print(f"Buscando libros del género: {genero}")
bibliotecaNacional.buscar_libro_por_genero(genero)

# todos los libros
print(f"-"*50)
print(f"Mostrando todos los libros en la biblioteca:")
bibliotecaNacional.mostrar_todos_los_libros()