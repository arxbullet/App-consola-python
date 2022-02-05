#MODULOS
#_____________________________________________
#SIRVEN PARA EMPAQUETAR CODIGO.
 
#crear un modulo
#1. crear un archivo.py y meter todas las funciones que necesite de ese modulo en el archivo

#2. importar el archivo 

import mymodulo

#3 usar las funciones del modulo importado

numero1 = input('ingresa un numero')
numero2 = input('ingresa un numero')

print(mymodulo.funcionsumar(numero1, numero2))

#si quiero importar una sola funcion del modulo

from mymodulo import funcionsumar

#si no quiero poner mymodulo. en cada funcion : 

from mymodulo import * 

#importar modulos de python por defecto

import datetime

today = datetime.date.today() #o date. otra funcion 

mes = today.month
año = today.year
dia = today.day

#toda la documentacion sobre estos modulos predefinidos estan en 
#la documentacion de python 

#modulo de matematicas 

import math 

print('la raiz cuadrada de 10', math.sqrt(10))

print('el numero pi es ', math.pi)

#modulo random 

import random

print('numero aleatorio entre 1 y 20 ', random.randint(1, 20))

#PAQUETES
#_____________________________________________
#SIRVEN PARA EMPAQUETAR MODULOS.

#crear paquete
#creo una carpeta y adentro creo un archivo _init_.py y con eso mi carpeta ya es un paquete
#luego creo un archivo.py para cada modulo del paquete

#importar el paquete

from mipaquete import modulodemipaquete

#si tengo muchos modulos puedo hacer lo siguiente

from mipaquete import modulodemipaquete, modulo2

# para importarlos todos 

from mipaquete import * 

#instalar paquetes o modulos de python 
# ingreso a la carpeta del proyecto y ejecuto pip install modulo 
 