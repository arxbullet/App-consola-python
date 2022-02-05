"""
proyecto python y msql

app de notas con login

app de consola
abrira asistente 
tendra opciones login y registro
si elegimos registro creara un usuario en la bd
si elegimos login, identificara al usuario y preguntara
crear nota, mostrar nota, borrar nota.
"""
#______________________________________
from usuarios import acciones
import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = '',
    database = 'master_python'
)

print("""
ACCIONES DISPONIBLES
-registro
-login
""")


accion = input('que quieres hacer?')
"""
if accion == 'registro':
    print('\nvamos a registrarte en el sistema')

    nombre = input('ingresa tu nombre')
    apellido = input('ingresa tu Apellido')
    email = input('ingresa tu email')
    passwd = input('ingresa tu passwd')


elif accion == 'login':
    print('\ninicio de sesion')
    email= input('ingresa tu email')
    passwd = input('ingresa tu contraseña')"""

# aca se hara lo mismo con modulos y paquetes para no alargar demasiado el codigo

hasEl = acciones.Acciones()


if accion == 'registro':
   hasEl.registro()

elif accion == 'login': 
   hasEl.login()