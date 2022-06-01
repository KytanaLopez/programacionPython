#Ejercicio No. 6 Ciclo for

rango=range(1,6)

for i in rango:
    print(i)

cadenaString='Calletana'

for letra in cadenaString:
    print(letra)

for i in range(2,11,2):
    print(i)

print('Imprimir los número impares del 0-10')

for i in range(1,11,2):
    print(i)

frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombreFruta, color in frutas.items():
    print(nombreFruta, "es de color", color)

print('Iterar sólo por los key')
for nombreFruta in frutas.keys():
    print(nombreFruta)

for colorFruta in frutas.values():
    print(colorFruta)

#Recuerda que también puedes tener for con else