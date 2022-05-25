def convertirmillasakm(millas:float):
    return (f'Las {millas} convertidas a kilómetros es: {millas*1.60934}')

def convertirkmamillas(kilometros:float):
    return (f'Los {kilometros} convertidos a millas son: {kilometros*0.621371}')

#Menú de opciones

opcion_menu=input('********************Menú Principal***********\n'
                  '1 - Convertir millas a kilómetros\n'
                  '2 - Convertir kilómetros a millas\n'
                  '0 - Salir\n'
                  'Digite la opción a elegir: '    )

while opcion_menu!='0':
    if opcion_menu=='1':
        print('**********Entró a la opción 1 - Convertir millas a kilómetros***************** ')
        millas=float(input('Digite las millas: '))
        print(convertirmillasakm(millas))
    elif opcion_menu=='2':
        print('**********Entró a la opción 2 - Convertir kilómetros a millas***************** ')
        kilometros=float(input('Digite los kilómetros: '))
        print(convertirkmamillas(kilometros))
    else:
        print('Usted debe digitar una opción válida')
    opcion_menu=input('********************Menú Principal***********\n'
                  '1 - Convertir millas a kilómetros\n'
                  '2 - Convertir kilómetros a millas\n'
                  '0 - Salir\n'
                  'Digite la opción a elegir: '    )