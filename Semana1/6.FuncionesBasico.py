def sumar(a:int, b:int):
    return (f'La suma es: {a+b}')

def tipo(a, b, c):
    return (f'El tipo de la variable a ({a}) es: {type(a)}, y el tipo de la variable ({b}) es: {type(b)}, el tipo de datos de la variable c ({c}) es: {type(c)} ')

def mayor(listaa):
    return (f'El mayor número de esa lista es: {max(listaa)}')

def menor(listaa):
    menor_lista= min(listaa)
    return menor_lista

def ambos(listaa):
    return print(f'El mayor de la lista es: {max(listaa)} y el menor de la lista es: {min(listaa)}')

def sumalista(listaa):
    return print(f'La suma de los elementos de la lista es: {sum(listaa)}')

a=float(input('Digite el número uno: ') )
b=float(input('Digite el número dos: ') )
c=input('Digite un texto')
print(sumar(a,b))
print(tipo(a,b,c))

#Lista
listaa=[3,4,5,6,7]
print(f'La lista ingresada es: {listaa}')
print(mayor(listaa))

print('El menor de la lista es: ', menor(listaa))
ambos(listaa)

print(help(print))

sumalista(listaa)