a=int(input('Por favor digite el primer número: '))
b=int(input('Por favor digite el segundo número: '))
c=int(input('Por favor digite el tercer número: '))
d=int(input('Por favor digite el cuarto número: '))

if a>b and a>c and a>d:
    print('El número mayor es: ', a)
else:
    if b>c and b>d:
        print('El número mayor es: ', b)
    else:
        if c>d:
            print('El número mayor es: ',c)
        else:
            print('El mayor es el número', d)