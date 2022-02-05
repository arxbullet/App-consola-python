"""from coche import Coche

carro = Coche('amarillo', 'renault', 'modelo 2020')


print(carro.getInfo())

# detectar el tipado de un objeto 

if type(carro) == Coche : 
    print('es un carro')
else : 
    print(' no es un objeto')

print(carro.__soyprivado___) # esto no funciona
print(carro.getPrivado()) # esto si funciona para obtener atributos privados"""

import clases 

persona = clases.Persona()

persona.setNombre('victor')
persona.setApellido('robles')
persona.setAltura('180')
persona.setEdad(25)

informatico = clases.Informatico()

informatico.setNombre(' juanito informatico')

informatico.getLenguajes() # metodo desde clase informatico 
informatico.Hablar() # metodo desde clase persona 