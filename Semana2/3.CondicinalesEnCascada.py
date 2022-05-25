num=int(input('Por favor digite un número entero: '))

if num<0:
    num=num*(-1)
if num >=0 and num<=9:
    print('El número tiene 1 dígito')
else:
    if num>=10 and num<=99:
        print('El número tiene 2 cifras')
    else:
        if num>=100 and num<=999:
            print('El número tiene 3 cifras')
        else:
            if num>=1000 and num<=9999:
                print('El número tiene 4 cifras')
            else:
                print('El número tiene más de 4 cifras')