n = int(input('Digite el número: '))
rango= range(1,n)
con=0

for i in rango:
    if n%i==0:
        con+=1

if con>2:
    print(f'El número {n} NO es primo')
else:
    print(f'El número {n} ES primo')

#Ésta es otra forma como está en el DFD

n = int(input('Digite el número: '))
rango=range(2,n+1)

print('Otra forma de conseguir los números pares')
for d in rango:
    r=n%d
    if r==0:
        if d==n:
            print(f'El número {n} ES primo')
            d=n
        else:
            print(f'El número {n} NO es primo')
            d=n
            break