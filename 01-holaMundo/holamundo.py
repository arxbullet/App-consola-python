print('hola mundo')
#comentario unilinea con hashtag
"""
comentario multilinea 
print('hola mundo2')
"""
#   VARIABLES
#_______________________________________________

variableX = 'esta es una variable'

concatenacion = variableX + " " + 'concatenada' 

concatenacionF = (f"{variableX}{concatenacion}")

concatenacionFormateada = ('hola esto es un ejercicio y {}'.format(variableX))

# resultado :  print(concatenacionF, concatenacionFormateada)

#  TIPOS DE DATOS
#________________________________________________________________________

nada = None # like null
type(nada) #mostrar tipo de dato
cadena = 'string'
entero = 99
floantente = 0.1
booleano = False
lista = []
listastring = [22, 'hola']
tupla = ('master', 11) #la tupla no cambia
diccionario = {'primero': 'vale', 'segundo' : 1 } #como los objetos 
rango = range(2) #rango del 0 al 2
datoByte = b'probando' #al poner una b frente el string p valor lo convierto a byte,

#no puedo concatenar strings con ints, entonces tengo que convertir los datos antes
numeritoString =str(1)
stringAnumerito = int(numeritoString)
numeritoafloat = float(stringAnumerito)

# CURIOSIDADES

textoEnComillas = " 'master' "
textoEnComillas2 = "\"Texto\" "
espacio =  textoEnComillas2 + "\n" + 'python'
tabulacion = textoEnComillas2 + "\t" + 'python'

#    OPERADORES
#___________________________________________________________
"""
ARITMETICOS
= : asignacion
- : menos
* : multiplicacion
/ : division
//: division con entero
% : resto
**: potencia

ASIGNACIÓN
+= aumento 
-= decremento
ejemplo : 1 += 5 , esto da 6 

COMPARACIÓN
== : igual
!= : distinto
< : mayor
> : menor
>= : menor igual
<= : mayor igual

COMPARADORES DE BIT
& :	Realiza bit a bit la operación AND en los operandos EJ: 	a & b = 2 (Binario: 10 & 11 = 10)
| :	Realiza bit a bit la operación OR en los operandos EJ:      a | b = 3 (Binario: 10 | 11 = 11)
^ : Realiza bit a bit la operación XOR en los operandos EJ:     	a ^ b = 1 (Binario: 10 ^ 11 = 01)
~ : Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando  EJ:     	~a = -3 (Binario: ~(00000010) = (11111101))
>> : Realiza un desplazamiento a la derecha bit a bit.
     Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha
     EJ:     	a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
<< : Realiza un desplazamiento a la izquierda bit a bit. 
     Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha

LOGICOS
and : y 
or : o
not: no

"""

#      ENTRADA Y SALIDA DE DATOS
#_______________________________________________________

variableparaguardarinfo = input('porfavor mete tu nombre \t')#para que el usuario ingrese datos por teclado 
print(f'hola {variableparaguardarinfo}')

#     CONDICIONALES 
#_____________________________________

condicion = input('pon un numero')


if int(condicion) == 1 : 
    print('escojiste el 1, muy basico')
    condicion = input('tienes una segunda oportunidad, ingresa otro numero')
    if int(condicion) == 2 : 
        print('predecible')

if int(condicion) > 5 & int(condicion) != 1 : print('wena, mayor a 5')
if int(condicion) < 5 & int(condicion) > 1 : print('no 1 pero igual bajo')
elif int(condicion) : print('gracias por participar')
else: print('tienes que haber puesto 0 verdad?')

#     BUCLES
#_____________________________________

contador = 0

for contador in range(0, 5): 
    print('voy por el numero '+str(contador))
    if int(contador) == 3 : 
        print('adios')
        break
    else : print('numeros finalizados')

whileContador = 0

while whileContador <= 10 : 
    input('ingresa un otro numero')
    if int(whileContador) == 1 : break
    else : print('okey'+str(whileContador))   
    whileContador += 1

