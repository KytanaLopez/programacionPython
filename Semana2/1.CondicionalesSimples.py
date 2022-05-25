a=4
b=6
if a>b:
    print('El número mayor es: ', a)
else:
    print('El número mayor es: ', b)


print('Sin el else')
if a>b:
    print('El número mayor es: ', a)

print('Por favor digite la hora en formato militar')
hora=int(input())

if hora>=12:
    print(f'Son las {hora} PM')
else:
    print(f'Son las {hora} AM')