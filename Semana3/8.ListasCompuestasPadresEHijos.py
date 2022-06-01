#Ejercicio No. 9 "Listas compuestas - Padres e hijos"
padres=[]
hijos=[]
rango=range(0,3)
for i in rango:
    nombrePadre=input('Por favor digite el nombre del padre: ')
    nombreMadre=input('Por favor digite el nombre de la madre: ')
    padres.append([nombrePadre,nombreMadre])
    cantidadHijos=int(input('Cuántos hijos tiene la familia: '))
    hijos.append([])
    rangoHijos=range(0,cantidadHijos)
    for j in rangoHijos:
        nombreHijo=input('Por favor digite el nombre de su hijo(a): ')
        hijos[i].append(nombreHijo)
for i in rango:
    print(f'Nombre del padre: {padres[i][0]}')
    print(f'Nombre del madre: {padres[i][1]}')
    for j in range(len(hijos[i])):
        print(f'Hijo(a): {hijos[i][j]}')
print('Listado de padres con sus hijos')
for i in rango:
    print(f'Nombre del padre {padres[i][0]}')
    print(f'Cantidad de hijos: {len(hijos[i])}')