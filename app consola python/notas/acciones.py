import notas.notas as modelo

class Acciones:

    def crear(self, usuario): 
        titulo = input('ingresa el titulo de la nota \n')
        descripcion = input('ingresa la descripcion de la nota \n')

        nota = modelo.Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >=1 : 
            print('nota guardada correctamente')

        else:
            print('algo ha salido mal')

    def mostrar(self, usuario): 
        nota = modelo.Nota(usuario[0], '', '')
        listaAMostrar= nota.listar()

        for n in listaAMostrar :
            print('\n*************')
            print(f'titulo : {n[2]}')
            print(f'descripcion : {n[3]}')
            print('\n*************')

    def eliminar(self, usuario):
        titulo = input('introduce el titulo a borrar')
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.borrar()

        if eliminar[0] >= 1 :
            print('se ha borrado correctamente')

        else : 
            print('ha ocurrido un error')
        

