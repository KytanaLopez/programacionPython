def mayor(lista:list):
    return f'El mayor número de la lista es: {max(lista)}'

def menor(lista):
    #menorr=min(lista)
    return 'El menor número de la lista es: '+ str(min(lista))

lista=[4,8,9,2]

print(lista)

for i in lista:
    print(i)

print(mayor(lista))
print(menor(lista))