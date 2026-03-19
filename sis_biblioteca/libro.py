class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        
    @property
    def titulo(self):
        return self._titulo
      
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo
      
    @property
    def autor(self):
        return self._autor
      
    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor
      
    @property
    def genero(self):
        return self._genero
      
    @genero.setter
    def genero(self, nuevo_genero):
        self._genero = nuevo_genero
        
    