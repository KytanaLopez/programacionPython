#Ejercicio No. 3... La sentencia break

variable = 10

while variable > 0:#True#True#True#True#True
    print('Actual valor de variable:', variable)#10#9#8#7#6
    variable = variable -1#9#8#7#6#5
    if variable == 5:#False#False#False#False#True
        break

#Ejercicio No. 4 ... La sentencia continue

variable = 10

while variable > 0:#True#True#True#True#True#True#True#True#True#True#False
    variable = variable -1#9#8#7#6#5#4#3#2#1#0
    if variable == 5:#False#False#False#False#True#False#False#False#False#False
        continue
    print('Actual valor de variable:', variable) # no imprime el 5#9#8#7#6#4#3#2#1#0
