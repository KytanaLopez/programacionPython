#Ejercicio No. 11 "Conjuntos"

conjunto={2,1,3,(4,6),1}

lista=[2,1,3,4,6,1]

print(conjunto)

print(lista)


print(type(conjunto))


conjuntoA=set([1,2,3,4])

print(conjuntoA)
print(type(conjuntoA))


for valor in conjunto:
    print(valor)

#Métodos

#add()

conjuntoDatos={7,1,2,3,5,8,9}

conjuntoDatos.add(10)

print(conjuntoDatos)

#clear()

conjuntoDatos.clear()

print(conjuntoDatos)

conjuntoA={1,2,3,4}
conjuntoB={2,4,6,8}

print(conjuntoA.intersection(conjuntoB))