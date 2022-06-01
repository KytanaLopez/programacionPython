#Ejercicio No.7 --- Listas paralelas

nombres=[]
edades=[]

rango=range(0,5)

for i in rango:
    nombre=input('Por favor digite su nombres: ')
    edad=int(input('Por favor digite su edad: '))
    nombres.append(nombre)
    edades.append(edad)

print('Las personas mayores a 18 años son: ')

for i in rango:
    if edades[i]>=18:
        print(nombres[i])