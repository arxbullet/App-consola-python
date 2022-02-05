#capturar excepciones y manejar errores

"""
nombre = input('escribe tu nombre')
"""
#que pasa si no se ingresa ningun nombre? tendria un string vacio

"""
if len(nombre) > 1 : 
    nombreUsuario = 'el nombre del usuario es ' + nombre
"""
#por mas que yo verifique que nombre tenga longitud mayor a 1, aun asi este codigo puede fallar
#para eso debo usar un try and except 
"""
try: 
    
    nombre = input('escribe tu nombre')
    if len(nombre) > 1 : 
        nombreUsuario = 'el nombre del usuario es ' + nombre
        print(nombreUsuario)

except: 

    print('ha ocurrido un error') #esto manejara el error 

else : 
    
    print( 'todo ha funcionado correctamente ') #esto se ejecutara si funciona el try

finally : 

    print('fin de la iteracion') #esto siempre se va a ejecutar

"""
#multiples errores : 

"""numero =  int(input('numero para elevarlo al cuadrado'))

print('el cuadrado de un numero es ' + str(numero*numero))"""

# en este codigo puedo tener varios errores, error de tipo, error de que este vacio, etc 
# para capturar todos los errores haremos lo sgte
"""
try : 
    numero =  int(input('numero para elevarlo al cuadrado'))

    print('el cuadrado de un numero es ' + str(numero*numero))

except TypeError:
    print('debes ingresar un tipo numero ')

except : 
    print('introduce un numero correcto')

except Exception as e: 
    print('ha ocurrido un error ', type(e).__name__)

"""

# excepciones personalizados

try:

    nombre = input('introduce nombre')
    edad = int(input('introduce edad'))

    if edad < 5 or edad > 110:
        raise ValueError('la edad introducidad no es real ') # personaliza un value error 

    elif len(nombre) <= 1 : 
        raise ValueError('el nombre no esta completo')

    else:
        print(f'bienvenido al master en python {nombre}')

except ValueError:    # capturo los value error
    print('Introduce los datos correctamente') 


except Exception as e : 
    print('existe un error', e)

