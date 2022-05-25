frase='             La programación es lo máximo      '
print(f'Si espacios sería: {frase.strip()}')

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))
print(linea.startswith('q'))
print(linea.lower().startswith('q'))

data='De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion=data.find('@')
print(enlaposicion)

camellos = 42
print('%d'%camellos+'a')
print('%d'%camellos+'b')
print(type(camellos))

print(f'Esto está tabulado A\tB y ésto está en salto de línea \n salto de línea')

cadena='un uno, un dos, un tres'
print(cadena)
print('Cuántas veces aparce el substring un')
print(cadena.count('un'))
print(cadena.replace('un','una'))
print(cadena)

print("El valor es {}".format(12))
valor1=12
print('El azul del cielo' + ' es muy bonito' + str(valor1))
print(cadena*3)

mensaje='Hola '
mensaje+='Mundo '
mensaje+='En python '

print(mensaje)