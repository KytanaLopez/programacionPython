#Ejercicio No. 6.. Lista

lista=[1,2,3,4,5]

lista2=['nombres', 'apellidos']

listas3=[1,2,'nombres']

listas4=[[1,2,3],5]


print(listas4[1])

#Rangos --- trozos

print(lista[1:4])

listaEjemplo = [1, 2.5, 'DevCode', [5,6] ,4]

print(listaEjemplo[0:5:2])

print('El tamaño de la lista es: ', len(listas4[0]))

#Métodos
#append()
#agrega un elemento al final de la lista

"""listaUsuario=[]

nombre=input('Digite su nombre : ')
apellido=input('Digite su apellido : ')

listaUsuario.append(nombre)
listaUsuario.append(apellido)

print(listaUsuario)"""

#Método count()
#Contar la cantidad de veces que aparece cierto elemento en mi lista

listaUno=[2,3,4,2,5,6,7,9]

print('Lista original', listaUno)
print(f'El número dos aparecece {listaUno.count(2)} ')

#Método extend()
#Agregar iterables al final de la lista

rango=range(5,8)
listaUno.extend(rango)
print(f'Agregando con extend un rango de números {listaUno}')

#Médoto index()
#Devuelve el índice del elemento

print(f'El índice del elemento 4 es: {listaUno.index(2)}')

#Método insert()
#Insertar un elemento en un índice indicado

listaUno.insert(2,2.5)
print(f'Insertamos elemento 2.5 en el índice 2, la nueva lista es: {listaUno}')

#Método pop()
#Devuelve y elimina el último elemento de la lista

print(f'El último elemento de la lista es: {listaUno.pop()}')
print(f'La nueva lista es: {listaUno}')

#Método remove()
#Elimina la primera aparición de un elemento en la lista

listaUno.remove(2)
print(f'La nueva lista es: {listaUno}')

#Método reverse()
#Invierte el orden de la lista

listaUno.reverse()
print(f'La nueva lista con reverse {listaUno}')

#Método sort()
#Ordenar los elementos de la lita de menor a mayor
listaUno.sort()
print(f'La lista ordenada es: {listaUno}')
listaUno.reverse()
print(f'Lista ordenada de mayor a menor: {listaUno} ')
