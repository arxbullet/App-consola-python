import datetime
#from sqlite3 import connect
import usuarios.conexion as conexion
import hashlib

connect = conexion.conectar()
database =  connect[0]
cursor = connect[1]

class Usuarios : 

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre =  nombre
        self.apellido = apellido
        self.email = email
        self.passwd = passwd

    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseña 
        cifrado = hashlib.sha256()

        cifrado.update(self.passwd.encode('utf8'))#cifrar algo en bytes(no se pueden cifrar strings)

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s , %s, %s)"
        usuario = self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha #guarda el string y no los bytes
            
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]  

        except: 
            result = [0, self]

        return result

    def identificar(self):

        sql  = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()

        cifrado.update(self.passwd.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest())

        #ejecutar la consulta con todos los datos

        cursor.execute(sql, usuario)
        result = cursor.fetchone() 
        return result

       
    
