#Ejercicio No. 11 "Tuplas"
#Dict --- {key:value}
#List --- [1,2,3,4]
#Tuplas --- (1,2,3,4) ó 1,2,3,4

tupla=(1,2,3,4,5,4)
tupla1=1,2,3,4

print(type(tupla))
print(type(tupla1))

tuplaLetras='a','e','i','o','u'

tuplaUnElemento='a',
print(tuplaLetras)

print(type(tuplaUnElemento))

print(tupla[0])

#Tuplas son inmunables

#tupla[0]=2

#Utilizar lista de tuplas con diccionarios

diccionario = {1020:10, 'b':1, 'c':22}
print(diccionario)
t = list(diccionario.items()) #items(), devuelve una lista de tuplas
print(t)

#Métodos
print(tupla)
#Método count()

print(f'La cantidad de veces que aparece el cuatro es: {tupla.count(4)}')

#Método index()

print(f'El índice del número 2: {tupla.index(2)}')