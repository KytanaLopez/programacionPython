import math
import math as funcionesMatematicas
from math import pi
from math import *

print('Área de un círculo cuyo radio es 4')
radio=4
areacirculo=((math.pi)*(radio**2))
print(areacirculo)

print('Digite un número')
num=int(input())
valorAbsoluto=math.fabs(num)

print(f'El valor absoluto de {num} es: {valorAbsoluto}')

print('Entero mayor y entero menor de un número flotante')
xFloat=float(input('Digite el número'))

print(f'El entero mayor es: {math.ceil(xFloat)} , el entero menor es: {math.floor(xFloat)}')

#Cuando importo con from, no utilizo el .

r=2*pi
print(f'El valor de r con pi importado con from es: {r}')

print('Math con el alias funcionesMatematicas')

radio=2*(funcionesMatematicas.pi)

print(radio)

print(0o123)
print(0x123)

#Módulos...
# Con el punto (.) usted puede acceder a cada una de las funciones de ese módulo

r=2
areaCirculo=round((funcionesMatematicas.pi)*(r**2),4)#alias de Math
print(areaCirculo)

#Otra forma de importar módulos
#from, no utilizo el punto porque ya importe mi función
r=2
areaCirculo=round((pi)*(r**2),4)
print(areaCirculo)
