

""""
Ordena las torres dando como salida aquella de más altura para las que las dos sean iguales
T1 = Lista de torre1
T2 = Lista de torre2
"""""
def OrdenarTorres(T1,T2):
    global asignaciones
    global comparaciones
    asignaciones, comparaciones = 0,0

    restantesT1 = len(T1)-1                                   #Preguntar si esto es una asignación
    restantesT2 = len(T2)-1                                   #Preguntar si esto es una asignación
    asignaciones+= 2

    print(T1,T2)
    TF = []
    while restantesT1 >= 0 and restantesT2 >= 0:
        eliminadas_en_T2 = contarEliminados(T1[restantesT1],T2,restantesT2)     #Preguntar si esto es una asignación
        eliminadas_en_T1 = contarEliminados(T2[restantesT2],T1,restantesT1)
        asignaciones+= 2
        print(restantesT1, restantesT2, eliminadas_en_T1, eliminadas_en_T2)

        #Posible mejora de codigo reduciendo repetición y con busqueda (tambien se puede comparar si se eliminan más que en el anterior y poner un flag y evitar hacer eliminaciones del otro)
        if eliminadas_en_T1 < eliminadas_en_T2:
            TF.append(T2[restantesT2])                                #Preguntar si esto es una asignación
            asignaciones+=1

            restantesT1-=eliminadas_en_T1+1
            restantesT2-=1
        if eliminadas_en_T1 > eliminadas_en_T2:
            TF.append(T1[restantesT1])                                #Preguntar si esto es una asignación
            asignaciones+=1

            restantesT2-=eliminadas_en_T2+1
            restantesT1-=1
        if eliminadas_en_T1 == eliminadas_en_T2:
            if restantesT2 >= restantesT1:
                TF.append(T1[restantesT1])                            # Preguntar si esto es una asignación
                asignaciones+=1

                restantesT2 -= eliminadas_en_T2 + 1
                restantesT1 -= 1
            else:
                TF.append(T2[restantesT2])  # Preguntar si esto es una asignación
                asignaciones+=1

                restantesT1 -= eliminadas_en_T1 + 1
                restantesT2 -= 1


    return TF



"""""
Cuenta la cantidad de piezas que habría que eliminar para igualar
pIgualar = Pieza a igualar
T2 = Lista con la torre 2
i = posición de la torre 2 en la que hay que buscar
@return eliminadas = cantidad de piezas eliminadas de la torre contraria
"""""
def contarEliminados(pIgualar,T,i):
    global asignaciones
    global comparaciones

    eliminadas = 0
    while pIgualar != T[i] and i >= 0:
        comparaciones += 1
        eliminadas+=1
        if i == 0:
            eliminadas = len(T)+1                          #El tamaño máximo del vector indica que no ha encontrado su pareja PREGUNTAR SI ES UNA ASIGNACION
            asignaciones += 1
        i-=1
    comparaciones += 1
    return eliminadas


"""
Programa Principal
"""

fichero = open("entrada.txt")
ficheroS = open("salida.txt","w")

linea = fichero.readline()
caso = 1

global asignaciones
global comparaciones

while linea != "0 0":

    "Obtenemos la lista de las torres y la pasamos a enteros"
    torre1 = [int(x) for x in fichero.readline().strip('\n').split(' ')]
    torre2 = [int(x) for x in fichero.readline().strip('\n').split(' ')]
    linea = fichero.readline()
    torreFinal = OrdenarTorres(torre1,torre2)
    longitudFinal = len(torreFinal)

#Preguntar por tildes
    ficheroS.write(f'''Caso de prueba: {caso}           
Numero de piezas: {longitudFinal}
Asignaciones: {asignaciones}
Comparaciones: {comparaciones}
Solucion:''')
    while longitudFinal> 0:
        ficheroS.write(f" {torreFinal[longitudFinal-1]}")
        longitudFinal-=1
    ficheroS.write("\n\n")

    caso+=1


fichero.close()
ficheroS.close()