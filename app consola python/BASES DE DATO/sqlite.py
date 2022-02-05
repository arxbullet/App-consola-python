# el modulo ya viene instalado en python y nos permite
#trabajar con una bd que se guarda en un archivo

import sqlite3

# conexion

conexion= sqlite3.connect('pruebas.bd')  #le paso el nombre de mi bd

#crear cursor para ejecutar consultas

cursor= conexion.cursor()

#crear tabla

cursor.execute('CREATE TABLE IF NOT EXISTS productos('+
'id INTEGER PRIMARY KEY AUTOINCREMENT ,' +
'titulo VARCHAR(255), '+
'descripcion text,' +
'precio INT(100)'
')') # lenguaje sql normal

#tambien puedo ejecutar sentencias sql comentariadas con bloques normales

cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255),
        descripcion text, 
        precio INT(255)
    );
         """)
 
#insertar datos
cursor.execute('INSERT INTO productos VALUES (null, primer producto, producto nuevo, 0000)')
conexion.commit()

#listar datos

cursor.execute('SELECT¡ *  FROM productos;')

productos = cursor.fetchall() # me entrega todos los resultados 

for producto in productos : 
    print('titulo : ' + producto[1])
    print('/n')

producto = cursor.fetchone() # me entrega el primer resultado

# Borrar registros 
cursor.execute('DELETE FROM productos')

#insertar muchos registros de golpe 

productos = [
    ('null', 'ordenador portatil', 'buen pc', 100)
 ]

cursor.executemany('INSERT INTO productos VALUES (null, ?, ? , ?)',productos )
conexion.commit()

#guardar cambios
conexion.commit()

#cerrar conexion 

conexion.close()