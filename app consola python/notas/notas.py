import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota: 
    
    def __init__(self, usuario_id, titulo='' , descripcion=''):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        try:
            sql = 'INSERT INTO notas VALUES (null, %s, %s, %s, NOW())'
            nota = (self.usuario_id, self.titulo, self.descripcion)

            cursor.execute(sql, nota)
            database.commit()

            result = [cursor.rowcount, self]

        except Exception as e:
            print(type(e))

            result = [0, self]

        return result

    def listar(self): 
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)

        result = cursor.fetchall()

        return result

    def borrar(self):
        
        try:
            sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "

            cursor.execute(sql)
            
            database.commit()

            result = [cursor.rowcount, self]

        except Exception as e:
            print(type(e))

            result = [0, self]

        return result
