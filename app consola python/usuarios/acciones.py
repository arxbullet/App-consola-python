import usuarios.usuario as user 
import notas.acciones as nota

class Acciones:
    def registro(self) :
        print('\nvamos a registrarte en el sistema')

        nombre = input('ingresa tu nombre')
        apellido = input('ingresa tu Apellido')
        email = input('ingresa tu email')
        passwd = input('ingresa tu passwd')

        usuario = user.Usuarios(nombre, apellido, email, passwd)

        registro = usuario.registrar()

        #comprobar registro

        if registro[0] >= 1 :
            print(f'Te has registro correctamente {registro[1].nombre}')

        else : print('ha ocurrido un error')

    def menuAcciones(self, usuario):
        print("""
        Acciones disponibles
        - crear nota ( crear )
        - mostrar notas ( mostrar )
        - eliminar nota ( eliminar )
        - salir ( salir )
        """)

        accion = input('ingresa una opcion')
        hazel = nota.Acciones()

        if accion == 'crear':
            print('vamos a crear una nota')
            hazel.crear(usuario)
            self.menuAcciones(usuario)

        elif accion == 'mostrar':
            print('vamos a mostrar una nota')
            hazel.mostrar(usuario)
            self.menuAcciones(usuario)

        elif accion == 'eliminar':
            print('vamos a eliminar una nota')
            hazel.eliminar(usuario)
            self.menuAcciones(usuario)
            
        elif accion == 'salir':
            print('vamos a salir')

    def login(self):
        print('\ninicio de sesion')

        try:

            email= input('ingresa tu email')
            passwd = input('ingresa tu contraseña')

            usuario = user.Usuarios('', '', email, passwd)

            login = usuario.identificar()

            if email == login[3] : 
                print(f'bienvenido {login[1]}')
                self.menuAcciones(login)
                

        except Exception as e :
            print('login incorrecto')
            print(type(e).__name__)

   


