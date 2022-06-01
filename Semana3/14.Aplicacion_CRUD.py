#Paso No.2 Inicializar el diccionario
tareas={
        '01':{
            'descripcion':'Ir a mercar',
            'estado':'pendiente',
            'tiempo':60
        },
        '02':{
            'descripcion':'Estudiar',
            'estado':'pendiente',
            'tiempo':180
        },
        '03':{
            'descripcion':'Hacer Ejercicio',
            'estado':'pendiente',
            'tiempo':50
        },

}

#Definición de funciones
def adicionarTareas(tareas, identificador, tareaNueva):
    tareas[identificador]=tareaNueva
    return tareas

def consultarTareas(tareas):
    for identificador, tarea in tareas.items():
        print(identificador,'--',end='')#end, es para que al final NO haga el salto de línea
        for atributos in tarea.values():
            print(atributos,'--',end='')
        print()

def buscarIdentificador(identificador,tareas):
    #convertir diccionario en un conjunto -- set
    conjuntoIdentificadores=set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

def actualizarTarea(tareas, identificador):
    #Pedir los nuevos datos
    nuevaDescripcion=str(input('Nueva Descripción: '))
    nuevoEstado=str(input('Nuevo Estado: '))
    nuevoTiempo=int(input('Nuevo Tiempo: '))

    #Asignamos al diccionario
    tareas[identificador]['descripcion']=nuevaDescripcion
    tareas[identificador]['estado']=nuevoEstado
    tareas[identificador]['tiempo']=nuevoTiempo

def eliminarTarea(tareas,identificador):
    conjuntoIdentificadores=set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        #Eliminar la eliminar -- pop eliminar por el key
        tareas.pop(identificador)
        print(f'La tarea con el identificador {identificador} se eliminó con éxito')
    else:
        print('No se ha encotntrado el identificador de la tarea a eliminar')
#Fin de funciones
#Menú de opciones

opcionMenu=True


while opcionMenu:
    print('--------------Aplicación CRUD----------\n'
            '1 - Adicionar Tareas - C\n'
            '2 - Consultar Tareas - R\n'
            '3 - Actualizar Tarea - U\n'
            '4 - Eliminar Tarea   - D\n'
            '5 - Salir')
    opcion=int(input('Ingrese la opción : '))
    #Paso 1, crear todas las opciones
    if opcion==1:
        print('-----------Adicionar Tareas-------------')
        #Paso 3. Recibir el identificador y los datos del diccionario interno
        identificador=str(input('Ingrese el identificador de la tarea: '))
        descripcion=str(input('Ingrese la descripción de la tarea: '))
        estado=str(input('Digite el estado de la tarea: '))
        tiempo=int(input('Ingrese el tiempo de realización: '))
        tareaNueva={'descripcion':descripcion,
                    'estado':estado,
                    'tiempo':tiempo}
        #La función adicionarTareas y la voy a llamar (tareas,identificador,tareaNueva)
        tareas=adicionarTareas(tareas,identificador,tareaNueva)
        #print(tareas)
    elif opcion==2:
        print('-------------Consultar Tareas-----------')
        #Paso 4 Hacer consultarTareas
        #consultarTareas(tareas)
        consultarTareas(tareas)

    elif opcion==3:
        print('----------Actualizar tareas-------------')
        #Pedir el identificador
        identificador=str(input('Por favor digite el identificador de la tarea a actualizar: '))
        #Saber si el identificar está, se hace una función buscarIdentificador
        if buscarIdentificador(identificador,tareas):
            #actualizar las tareas
            actualizarTarea(tareas,identificador)
        else:
            print('No se ha encontrado una tarea con ese identificador...')


    elif opcion==4:
        print('--------------Eliminar Tarea----------')
        #Solicitar al usuario el identificador de la tarea
        #Pedir el identificador
        identificador=str(input('Por favor digite el identificador de la tarea a actualizar: '))
        #Saber si el identificar está, se hace una función eliminarTareas(tareas, identificador)
        eliminarTarea(tareas,identificador)
    elif opcion==5:
        print('Dios le bendiga, ha salido del sistema...')
        opcionMenu=False

    else:
        print('No ha seleccionado una opción correcta')
    

