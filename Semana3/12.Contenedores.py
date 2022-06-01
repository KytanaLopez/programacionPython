#Ejercicio No. 12 "Contenedores"

diccionarioEstudiantes = {
    'E3454fdf':{
        'nombres': 'Laura',
        'apellido': 'Jaramillo',
        'acudientes': ['Andrea','Juan'],
        'promedio': 5.0
    },
    'Egg56dfg':{
        'nombres': 'Samir',
        'apellido': 'Gómez',
        'acudientes': ['Alejandro','Sofía'],
        'promedio': 5.0
    },
    'FHT43523':{
        'nombres': 'Sara',
        'apellido': 'Cabrera',
        'acudientes': ['Carlos','Amparo'],
        'promedio': 5.0
    },
    'Z4edkdf':{
        'nombres': 'Iván',
        'apellido': 'Arcila',
        'acudientes': ['Esposa'],
        'promedio': 5.0,
        123: 'Este estudiante es alérgico al maní'
    },
}

#print(diccionarioEstudiantes)

print(diccionarioEstudiantes['FHT43523'])

print('Recorrer e impirmir todo el contenedores')
for claves, valores in diccionarioEstudiantes.items():
    print(f'Código Estudiante: {claves}')
    print(f'Información : {valores}')

print('Recorrer e imprimir por las claves')

for claves in diccionarioEstudiantes.keys():
    print(f'Las claves de los estudiantes son: {claves}')


print('Recorrer e imprimir sólo la información de los estudiantes')

for valores in diccionarioEstudiantes.values():
    print(f'La información del estudiante : {valores}')

for codigoEstudiante, informacionEstudiante in diccionarioEstudiantes.items():
    print('Código del Estudiante : ', codigoEstudiante)
    print('Información del estudiante : \n ', informacionEstudiante )