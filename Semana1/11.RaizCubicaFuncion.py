def raizcubica(numero:float):
    resultado=numero**(1/3)
    return resultado


numero=float(input('Digite el número para hallar la raíz cúbica: '))

if numero<0:
    numero=numero*(-1)
    resultado=raizcubica(numero)
    resultado=resultado*(-1)
    print("La raíz cúbica del número es: ", resultado)
else:
    print("La raíz cúbica del número es :", raizcubica(numero))