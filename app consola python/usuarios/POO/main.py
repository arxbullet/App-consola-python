# definir una clase 

#ejemplo objeto de tipo coche

class Coche :

    color = 'rojo' # atributos o propiedades por defecto
    marca = 'ferrari' # vienen por defecto como publicos 
    modelo = '' # cuando estan como privados, solo se puede acceder a esos datos con metodo getter
    velocidad = 0
    caballaje = 0
    plazas = 2

# definir metodos 

    def acelerar(self): # usando la palabra self puedo acceder a mis atributos  
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad


# lo ideal no es definir metodos que accedan directamente a las propiedades
# por lo que es mejor usar metodos getter and setter

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

# crear objetos/ instanciar la clase

coche = Coche()

print(coche.marca, coche.color)
print(coche.velocidad) # puedo acceder a estas propiedades por que son publicas

coche.acelerar()

coche.acelerar()

coche.acelerar()

coche.acelerar()

print(coche.velocidad) # 4

coche.frenar()

print(coche.velocidad) # 3


# ya que las clases son moldes de multiples objetos, se peuden crear mas objetos 

coche2= Coche()

print(coche2.marca)

coche2.setColor('verde') # aunque sean objetos distintos puedo utilizar los mismos objetos

print(coche2.color)

print(type(coche2)) # type detectara que coche 2 es un objeto tipo clase 

