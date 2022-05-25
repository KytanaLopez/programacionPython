def convertirlibrasakg(libras:float)->str:
    pesokg=libras*0.453592
    return (f'{libras} libras convertidas en Kg son: {pesokg}')

libras=float(input('Digite su peso en libras: '))

print(convertirlibrasakg(libras))