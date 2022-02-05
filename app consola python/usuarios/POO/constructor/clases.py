# herencia : compartir atributos y metodos entre clases
# el constructor no se herencia automaticamente, para hacerlo : 
# super.__init__()

from _typeshed import Self


class Persona: 

    """nombre
    apellido
    altura
    edad"""

    def getNombre(self):
        return self.nombre
 
    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def Hablar(self) : 
        return 'estoy hablando'

    def Caminar(self):
        return 'estoy caminando'

class Informatico(Persona) : # heredo desde la clase persona pasando la clase en los lenguajes

    """lenguajes 
    experiencia """

    def __init__(self):
        self.lenguajes = 'HTML,CSS, JAVASCRIPT'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    