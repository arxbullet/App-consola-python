#DIRECTORIOS
#________________________________

#crear carpeta

import os , shutil

if not os.path.isdir('./micarpeta'):
    os.mkdir('./micarpeta')
else : 
    print('el directorio ya existe')

#copiar carpeta

rutaOriginal=('./micarpeta')
ruta_nueva= ('./micarpetaCopiada')

shutil.copytree(rutaOriginal, ruta_nueva)

#saber el contenido de mi carpeta
contenido= os.listdir('./micarpeta')

#eliminar carpeta

os.rmdir('./micarpetaCopiada')

print(contenido)