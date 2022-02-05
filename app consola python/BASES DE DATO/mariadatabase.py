import mysql.connector

#conexion

database =  mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'master_python'
)

# 

#¿la conexion ha sido correcta?

#print(database)

cursor = database.cursor()

#cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id INT(10) auto_increment not null,
    marcar VARCHAR(20) not null,
    modelo VARCHAR(20) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#insertar registros

cursor.execute("""
INSERT INTO vehiculos VALUES(null, 'opel', 'astra')
""")

database.commit()

