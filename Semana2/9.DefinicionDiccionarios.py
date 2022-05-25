diccionario={   'cedula':1065, 
                'nombre':'Calletana',
                'apellidos':'López',
                'profesion':'Ingeniera de Sistemas'}

print(diccionario)

print(diccionario['nombre'])

diccionarioUno={101:'Calletana López', 
                102:'Maria Baleta', 
                103:'José López'}

print(diccionarioUno)

#Otra forma de declarar

diccionarioDos={}
diccionarioDos['nota1']=3.5
diccionarioDos['nota2']=4.0
diccionarioDos['nota3']=3.2

print(diccionarioDos)

print(diccionarioUno[101])
suma=diccionarioDos['nota1']+diccionarioDos['nota2']+diccionarioDos['nota3']
print('La suma es: ', suma)

diccionarioUno[101]='Cayetana López Baleta'

diccionarioUno[104]='Juan Valdez'
print(diccionarioUno)

print('Iterando con un for ambos, clave y valor')

for key, value in diccionarioUno.items():
    print(key, value)

print('Iterar sólo por la clave')

for key in diccionarioDos.keys():
    print(key)

print('Iterar sólo por el valor')

for valor in diccionarioUno.values():
    print(valor)