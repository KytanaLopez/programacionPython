def redondear(num:float):
    #return f'El número {num}, redondeado a dos decimales es: {round(num,2)}'
    r=round(num,2)
    return 'El número '+ str(num) + ' , redondeado a dos decimales es: ' + str(r)

num=float(input('Digite un número punto flotante o decimal'))

print(redondear(num))