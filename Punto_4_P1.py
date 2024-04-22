import time

def Fibonnacci (x : int): #Defininimos la función para calcular la sucesión de Fibonnacci#
    if x <= 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return (Fibonnacci(x-1) + Fibonnacci(x-2))
            
if __name__ == "__main__" :
    j : int = int(input("Dijite cuantos números de la Sucesión de Fibonnaci desea: "))
    if j > 0 :

        start_time1 = time.time()
        for n in range (j):
            print(Fibonnacci(n), end=", ")
        end_time1 = time.time()
        print(f"Con funciones recursivas la función se demora {end_time1 - start_time1} segundos")
    
        start_time2 = time.time() 
        terminos_sucesion : int = j #Definimos la sucesión de Fibonnacci con ciclos for#
        primer_termino : int = 0
        segundo_termino : int = 1
    
        print(str(primer_termino) + ", " + str(segundo_termino), end=", ")
        for i in range ( 2, terminos_sucesion ):
            termino : int = primer_termino + segundo_termino
            print(str(termino), end=", " )
            primer_termino = segundo_termino
            segundo_termino = termino
        end_time2 = time.time()
        print(f"Con iteraciones la función se demora {end_time2 - start_time2} segundos")
    else:
        print("DIjite un número positivo")
    
    if abs((end_time1 - start_time1) - (end_time2 - start_time2)) > 0.5 : #Hallamos la diferencia de tiempo entre las funciones#
        print(f"Despues de {j} terminos la diferencia entre los tiempos se hace significativa")
    else:
        print(f"Despues de {j} terminos la diferencia no es tan significativa")