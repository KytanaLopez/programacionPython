#Ejercicio No. 8. Listas compuestas

lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#Imprimir un elemento (una de sus lista)

print(lista[2])

#imprimir los elementos que están dentro de listas internas

print(lista[2][1])

#imprimir los elementos de la lita contenida [0]

for i in range(len(lista[2])):
    print(lista[2][i])

#Recorrer todos los elementos de lista
print('Todos los elementos de la lista')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j])