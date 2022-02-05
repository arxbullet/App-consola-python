# FICHEROS
# ______________________
# para usar ficheros hay que usar un paquete llamado io 

from io import open 

#abrir archivo

#archivo = open("mipaquete/modulodemipaquete.py", "a+") pongo la carpeta y el archivo y luego los permisos
archivo = open("modulodemipaquete.txt", "a+")  #si le quito la ruta lo creara en la carpeta

import pathlib, shutil
#sirve para obtener rutas 

ruta = str(pathlib.Path().absolute()) + "/modulodemipaquete.txt"

archivo = open(ruta, "a+") #abrira el archivo con su ruta exacta

#escribir dentro del archivo 
'''
archivo.write("soy un texto metido desde python")
'''
#cerrar el archivo
'''
archivo.close() 

archivo_lectura =  open(ruta, 'r')
'''
#leer archivo 
'''
contenido = archivo_lectura.read()

print(contenido)
'''
#tambien puedo leerlo linea a linea y guardarlo en una lista
'''
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista :
    lista_frase= frase.split()
    print(lista_frase)
'''
#copiar ficheros 
ruta_nueva = str(pathlib.Path().absolute()) + "/modulodemipaquete2.txt"
shutil.copyfile(ruta, ruta_nueva) #poner en argumentos ruta actual y nueva 

#copiar a otra ruta 
ruta_Alternativa = str(pathlib.Path().absolute()) + "./mipaquete/modulodemipaquete.txt"
shutil.copyfile(ruta, ruta_Alternativa )

#otras funciones
"""
shutil.move(rutaantigua, ruta nueva) # esto sirve para mover archivos
"""

import os
#con este modulo eliminaremos un fichero

os.remove(ruta)

#comprobar sin un archivo existe

os.path.abspath("./") #entrega la ruta absoluta del archivo

ruta_comprobar = os.path.abspath("./")  + 'modulodemipaquete.txt'

if os.path.isfile(ruta_comprobar):
    print('existe')

else :
    print('no existe')