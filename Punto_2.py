# Vamos a tomar los ejercicios del punto 7 del Primer Taller #
def Promedio (*args) :
    if len(args) == 0 :
        return 0 # Si no hay argumentos el promedio es 0 esto es para evitar errores matematicos al dividir entre 0 #
    Suma = sum(args)
    promedio = Suma / len(args)
    return promedio
def Suma (*args):
    Suma = sum(args)
    return Suma
def PromedioMultiplicativo(*args):
    if len(args) == 0:
        return 0  # Si no hay argumentos el promedio es 0 esto es para evitar errores matematicos al dividir entre 0 #
    producto = 1
    for num in args:
        producto *= num
    promedio_multiplicativo = producto ** (1 / len(args))
    return promedio_multiplicativo



    
if __name__ == "__main__" :
    a : int = int(input("Dijite un número: "))
    b : int = int(input("Dijite un número: "))
    c : int = int(input("Dijite un número: "))
    d : int = int(input("Dijite un número: "))

    print(f"El promedio es {Promedio(a,b,c,d)}, la suma es {Suma(a,b,c,d)} y el promedio multiplicativo es {PromedioMultiplicativo(a,b,c,d)}")