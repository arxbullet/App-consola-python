# ARRAYS y TUPLAS
#__________________________________________
#para definir una lista la guardo con corchetes 
#una tupla es una lista que no puede ser cambiada

sumarTuplaaLista = list(('uno', 'dos' ,'tres'))
crearListaConRango = list(range(1,10))

#indices de las listas

sumarTuplaaLista[0] #esto sera igual a 'uno'
sumarTuplaaLista[1:2]  #esto traeria 'dos' y 'tres'
sumarTuplaaLista[1:]  #esto traeria todos los elementos despues del 1

sumarTuplaaLista[1] = 'unopuntocinco' #aca modifico el elemento uno de la lista

sumarTuplaaLista.append('cuatro') #agrego cosas a la lista

#recorrer lista , se puede usar bucles for y while
for i in sumarTuplaaLista: 
    print(f'{i}')

#listas multidimensionales

contactos = [
    ['juan', 'juan@mail.com'],
    ['luis', 'luis@mail.com']
]

contactos[0][0] #esto es igual a juan, juan@mail.com

#puedo recorrer estos casos con un for dentro de un for 

for contacto in contactos :
    for elemento in contacto:
        print(elemento)

print(contactos.index(['juan', 'juan@mail.com'])) #devuelve el indice del elemento que ingresamos

contactos.sort() #ordena nuestros arrays

contactos.insert(1, ['pedro', 'pedro@mail.com']) #agrega un elemento en cierto indice 
contactos.pop(0) #borra elemento de cierto indice

sumarTuplaaLista.remove('cuatro')#borra cierto elemento

sumarTuplaaLista.reverse() #da vuelta el orden de la lista

'cuatro' in sumarTuplaaLista #buscar dentro de un array

len(sumarTuplaaLista) #me da el numero de elementos

sumarTuplaaLista.count('unopuntocinco')#saber cuantas veces se repite un elemento

sumarTuplaaLista.extend(contactos) #sumar una lista a otra



#   DICCIONARIOS y sets
#_____________________________________________________________________________

set = {'one', 'two', 'three'} #es un conjunto de datos que no tiene orden ni indices

set.add('four')
set.remove('one')

#DICCIONARIO : almacena una clave y valor , como un objeto json pero tiene indices 

diccionario = {'nombre' : 'vale', 'nombre': 'juan'}

diccionario['nombre']

#________________________________________________________________________

diccionarioYListas = [
    {'nombre': 'pedrito',
    'email': 'pedrito.com'},
    {'edad': 90}
]

diccionarioYListas[0]['nombre'] #esto es igual a pedrito

