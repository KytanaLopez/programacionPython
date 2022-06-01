#Ejercicio No. 11 Tuplas "Cosméticos"
def Cosmeticos(ventas: list):
    ventacliente = {}
    for Identificador, NombreProducto, Descripcion in ventas:
        if ventacliente.get(Identificador) == None:
            ventacliente[Identificador] = []                                  
        ventacliente[Identificador].append((NombreProducto, Descripcion))                 
    print(ventacliente) #Ocultar al ejecutar
    return ventacliente

Cosmeticos([
    (2001,'Labial', 'Pintura de mujer Labial'),
    (2010,'Sombra','Sombra de ojos')])
print()
