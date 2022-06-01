#Ejercicio No. 2 Ciclo while

n = 5#5
while n > 0:#True#True#True#True#True#False
    print(n)#5#4#3#2#1
    n = n - 1#4#3#2#1#0"""

#while con else

#promedio=0.0
#total=0
#contar=0
promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))#3
while grado != -1:#True#True#Falso
    total = total + grado#3#8
    contar += 1#1#2
    grado = int(input(mensaje))#5#-1
else:
    promedio = total / contar#4
    print("Promedio de notas del grado escolar: " + str(promedio))#4
