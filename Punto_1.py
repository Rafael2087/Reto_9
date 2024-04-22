if __name__ == "__main__": # Se va a tomar el punto 1 del Reto 8 #
    print(f"Ejercicio 1 del reto 8")
    i : int = int(input("DIjite un número: "))
    CuadradoFuncion = lambda x: x**2 # Esta función nos permite calcular el cuadrado de un número #
    Cuadrado = CuadradoFuncion(i)
    print(f"El número {i} elevado al cuadrado es igual a {Cuadrado}")

    # Se va a tomar el punto 6 del reto 6 #
    print(f"Ejercicio 6 del reto 6")
    contagiados_inicial : int = int(input("Dijite la cantidad de contagiados inicialmente: "))
    dias : int = int(input("Dijite el número de días transcurridos: "))
    ContagiadosFuncion = lambda x , y : x * 2 ** y # Se define la función lambda para calcular el número de contagiados #
    Contagiados = ContagiadosFuncion(contagiados_inicial,dias)
    print(f"El número de contagiados despues de {dias} días es igual a {Contagiados}")

    # Se va a tomar el punto 5 del reto 6 #
    print(f"Ejercicio 5 del reto 6")
    capital_inicial : float = float(input("Dijite el capital inicial: "))
    porcentaje_interes : float = float(input("Dijite el porcentaje de interes (%): "))
    meses : int = int(input("Dijite la cantidad de meses: "))
    InteresFuncion = lambda x, y, z : x*(1 + y/100)**(z)
    Interes = InteresFuncion(capital_inicial,porcentaje_interes,meses)
    print(f"El valor total a pagar es de {Interes} $")