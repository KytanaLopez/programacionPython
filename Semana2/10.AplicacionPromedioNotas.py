def promedioNotas(dicNotas):
    sumatoria=0
    sumatoria+=dicNotas['nota1']
    sumatoria+=dicNotas['nota2']
    sumatoria+=dicNotas['nota3']
    sumatoria+=dicNotas['nota4']
    promedio= round((sumatoria/4),2)
    return promedio
    
dicNotas={}
dicNotas['nota1']=3.0565656
dicNotas['nota2']=4.05656545
dicNotas['nota3']=2.72232541
dicNotas['nota4']=3.523232332

print('El promedio es: ', promedioNotas(dicNotas))

#print('Otras formas')

def promedio(dicNotas):
    suma = 0
    for i in dicNotas:
        suma += dicNotas[i]
    return round(suma / len(dicNotas), 2)
  

dicNotas={}
dicNotas['nota1']=3.0565656
dicNotas['nota2']=4.05656545
dicNotas['nota3']=2.72232541
dicNotas['nota4']=3.523232332

print(f' El promedio de la nota es: {promedio(dicNotas)}')

#print('Otra forma')

def promedioNotas(dicNotas):
    return (dicNotas['nota1'] + dicNotas['nota2'] + dicNotas['nota3'] + dicNotas['nota4']) / 4

dicNotas={}
dicNotas['nota1']=3.0565656
dicNotas['nota2']=4.05656545
dicNotas['nota3']=2.72232541
dicNotas['nota4']=3.523232332

print('El promedio es: ', promedioNotas(dicNotas))