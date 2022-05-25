def cliente(informacion):
    if informacion['edad'] > 18:
        informacion['atraccion'] = 'X-Treme'
        informacion['apto'] = True
        if informacion['primer_ingreso'] == True:
            informacion['total_boleta'] = 20000*0.95
        else:
            informacion['total_boleta'] = 20000 
                     
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        informacion['atraccion'] = 'Carros chocones'
        informacion['apto'] = True
        if informacion['primer_ingreso'] == True:
            informacion['total_boleta'] = 5000*0.93
        else:
            informacion['total_boleta'] = 5000 
            
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        informacion['atraccion'] = 'Sillas voladoras'
        informacion['apto'] = True
        if informacion['primer_ingreso'] == True:
            informacion['total_boleta'] = 10000*0.95
        else:
            informacion['total_boleta'] = 10000
            
    else:
        informacion['atraccion'] = 'N/A'
        informacion['apto'] = False
        informacion['total_boleta'] = 'N/A'
        
  
    newdic = {
                'nombre':informacion['nombre'],
                'edad':informacion['edad'],
                'atraccion':informacion['atraccion'],
                'apto':informacion['apto'],
                'primer_ingreso':informacion['primer_ingreso'],
                'total_boleta':informacion['total_boleta']
    }
          
    
    return newdic

informacion = {}
informacion['id_cliente']=int(3)
informacion['nombre']='Calletana'
informacion['edad']=int(8)
informacion['primer_ingreso']=bool(True)

print(cliente(informacion))