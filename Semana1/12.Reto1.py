def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo>2:
        interest = (capital*0.03*tiempo)/12
        total = interest + capital
        return "Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(total)
        
    else:
        valuelost = capital*0.02
        totallost = capital - valuelost
        return "Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(totallost)

print(CDT("AB1012",1000000,3))
print(CDT("QW3456",5000000,2))