class Coche :

    color = 'rojo' 
    marca = 'ferrari'
    modelo = ''
    velocidad = 0
    caballaje = 0
    plazas = 2

    publico = 'soy publico'
    __soyprivado___ = 'soy un atributo privado'

    # constructor : cuando yo valla a crear un objeto un cosntructor me ayudara a inicializar 
    #sus atributos de forma personalizada

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color  = color 
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def getPrivado (self):
        return self.__soyprivado___

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
   
    def getInfo(self):
        info = '---------info---------'
        info += '/n Color: ' + str(self.getColor())

        # y asi con toda la info que quiera devolver 

