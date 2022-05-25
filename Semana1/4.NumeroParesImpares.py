num=int(input('Digite el número: '))
if num<0:
    print('Digite sólo números positivos')
else:
    if num//2*2==num:
        print(f'El número {num} ES PAR')
    else:
        print(f'El número {num} ES IMPAR')
#Otra forma
print('Ésta es otra forma, con el módulo de la división')

if num%2==0:
    print(f'El número {num} ES PAR')
else:
    print(f'El número {num} ES IMPAR')