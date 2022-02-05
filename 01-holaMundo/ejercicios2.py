# EJERCICIOS DE LISTAS, TUPLAS Y DICCIONARIOS
# ________________________________________________
'''
#ejercicio 1 
lista = list(range(1,8))
lista.sort()
for i in lista : 
    print(i)

print(f'esto es una lista de {len(lista)} longitud')

buscar = input('ingresa un numero para buscarlo')
busqueda = lambda lista :  int(buscar) in lista

print(busqueda(lista))

#EJERCICIO 2 
coleccion = []

#while

while len(coleccion) < 12 : 
    añadir = input('añade un numero')
    if isinstance(añadir, int):
      coleccion.append(añadir)
    else : print('el caracter no es un numero')

print(coleccion)

#for 

for i in range(1, 12) :
    coleccion.append(i)

print(coleccion)
'''
#ejercicio 3 

juegos = [
    {'categoria': 'aventura', 'listaDeJuegos': ['ASSINS', 'CRASH', 'PRINCE OF PERSIAN']},
    {'categoria': 'deportes', 'listaDeJuegos': ['FIFA 21', 'PRO 21', 'ROCKET LEAGUE']},
    {'categoria': 'accion', 'listaDeJuegos': ['GTA', 'COD', 'PUB']},
]

def mostrarJuegos():
    for i in juegos:
        print('_________________________')
        print(i['categoria'])
        print('_________________________')
        print(i['listaDeJuegos'])
        print('\n')

mostrarJuegos()