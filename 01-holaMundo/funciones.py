# FUNCIONES
# __________________________________________________________
# def es equivalente a function
# es recomendable definir todas las funciones primero arriba en el fichero
# y luego llamarlas en el orden deseado, tambien es recomendable que la funcion siempre devuelva un dato



def nombreDeMiFuncion(params):
    print(f'hola {params}')

#invocar funcion 
nombre = input('pon tu nombre again ')
nombreDeMiFuncion(nombre)

#parametros opcionales 
def optional(params = None):
    print(f'hola {params}')

# return 

def funcionReturn(params):
    return(f'hola {params}')

print(funcionReturn('vale')) #esto es igual a la funcion nombreDeMiFuncion

#funciones dentro de otras

def getNombre(nombre):
    texto = f'el nombre es {nombre}'
    return texto

def getApellido(apellido):
    texto = f'el apellido es {apellido}'
    return texto

def funcionDentroDeOtra():
    nombre  =  input('ingresa tu nombre')
    apellido  =  input('ingresa tu apellido')
    print(getNombre(nombre) +'\n' + getApellido(apellido))

funcionDentroDeOtra()

#funciones Lambda o anonimas

funcionLamda = lambda nombre : print(f'tu nombre es {nombre}')

funcionLamda('valentina')

#funciones predefinidas

'''
type(variable)
isIntance(variable o valor , tipo de dato)
print(variable)
len(“Hola Python”)	Determina la longitud en caracteres de una cadena. 	
.join('variable tipo lista')	Convierte en cadena utilizando una separación
split('cada palabra sera un elemento de la lista') Convierte una cadena con un separador en una lista	
.upper()	Convierte una cadena en Mayúsculas	texto = “Manuel es mi amigo”
.lower()	Convierte una cadena en Minúsculas	
range()	Crea un rango de números	
str()	Convierte un valor numérico a texto	str(22)	’22’
int()	Convierte a valor entero	
float()	Convierte un valor a decimal	
max()	Determina el máximo entre un grupo de números	
min()	Determina el mínimo entre un grupo de números	
sum()	Suma el total de una lista de números	
list()	Crea una lista a partir de un elemento como un rango
tuple()	Crea o convierte en una tupla
open()	Abre, crea, edita un elemento (archivo)	
ejemplo: 
with open(“Ejercicios/Ejercicio.py”, “w”) as variables:
variables.writelines(“Eje”)

ord()	Devuelve el valor ASCII de una cadena o carácter.	
round()	Redondea después de la coma de un decimal	
.strip() corta los espacios en blanco de una cadena
.find('elemento a encontrar') encuentra una palabra en una cadena o lista
.replace('elemento a remplazar', 'remplazo') remplaza elemento en una cadena o lista

'''

