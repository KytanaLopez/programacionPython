var_String='banana'

letraInicial=var_String[0]
letraFinal=var_String[-1]
longitud=len(var_String)
ultimaLetra=var_String[longitud-1]
tresPrimerasLetras=var_String[0:3]
trozoLetras=var_String[:3]
trozoLetras2=var_String[3:]
trozoLetras3=var_String[3:3]
trozoLetras4=var_String[3:4]
trozoLetras5=var_String[2:4]
variable='z'
aparecea=variable in var_String
print('La palabra es: ', var_String)
print(f'La letra inicial de la palabra es: {letraInicial}')
print('La letra final de la palabra es: ' + letraFinal)
print(f'Otra forma de hallar la última letra:{ultimaLetra} ')
print(f'La cantidad de letras que tiene la palabra es: {longitud}')
print(f'Las tres primeras letras de la palabra son: {tresPrimerasLetras} ')
print(f'El trozo de letras : [:3] {trozoLetras}')
print(f'El trozo 2 de letras [3:]{trozoLetras2}')
print(f'El trozo 3 de letras [3:3]{trozoLetras3} : vacío')
print(f'El trozo 4 de letras [3:4]{trozoLetras4}')
print(f'El trozo 5 de letras [2:4]{trozoLetras5}')
print(f'Si aparece esta subcadena es: {aparecea}')

palabra='La banana es dulce'

print(palabra)
print('Palabra en la posición cuatro')
print(palabra[4])

print(f'La longitud de la frase es: {len(palabra)}')

print(f'La última letra de la frase es:{palabra[-1]} ')

print(f'La última letra de la frase es: {palabra[len(palabra)-1]} ')

print(f'Las cuatro primeras letras de la frase son: {palabra[0:4]} ')
print(f'Las letras de la frase [6:12] son: {palabra[6:12]} ')
print(f'Las letras de la frase [8:17] son: {palabra[8:17]} ')
print(f'Las letras de la frase [8:8] son: {palabra[8:8]} ')
print(f'Si la letra a está dentro de la cadena')
letra='z'
print(letra in palabra)# True o False

if (letra in palabra):
    print(f'La letra {letra} está en la frase')
else:
    print(f'La letra {letra} NO está en la frase')

palabra_Uno='aananas'
palabra_Dos='banana'

print(palabra_Uno>palabra_Dos)

if palabra_Uno==palabra_Dos:
    print('Son iguales')
else:
    print('Son diferentes')


if palabra_Uno>palabra_Dos:
    print(f'La mayor es la palabra Uno {palabra_Uno}')
else:
    print(f'La mayor es la palabra Dos {palabra_Dos}')

variable='Calletana'

#print(dir(variable))
print('La cadena es: '+variable)
print(f'La cadena convertida a mayúsculas es: {variable.upper()}')
print(f'La cadena convertida a minúsculas es: {variable.lower()}')

palabra = 'banana'
index = palabra.find('b')
print('El índice de la letra es: ', index)