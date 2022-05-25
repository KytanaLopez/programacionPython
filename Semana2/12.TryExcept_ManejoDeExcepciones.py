try:
    a=int(input('Digite una variable tipo entera'))
    print(a)
except:
    print('Señor usuario ha habido un error en el sistema, por favor vuelva a iniciar')


try:
    a=int(input('Digite un número : '))
    b=int(input('Digite otro número  : '))

    print(a/b)
except:
    print('Ha ocurrido un error en la ejecución, por favor vuelva a intentarlo')

temperatura_fahr = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(temperatura_fahr)
    cel =  5.0 / (9.0 * (fahr - 32.0))
    print(cel)
except:
    print('Please enter a number')

try:
    cedula=input('Digite su cédula')
    longitud=len(cedula)
    print(longitud)
    if longitud>10:
        print('Su cédula no puede ser mayor a 10 dígitos o no puede contener letras')
    cedula=int(cedula)
except:
    print('No aceptado su número de cédula o no puede contener letras...')
