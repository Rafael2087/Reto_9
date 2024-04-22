def PotenciaRecursiva (x : int, y : int):
    if y == 0 :
        return 1
    else:
        return x*PotenciaRecursiva(x , y - 1)

if __name__ == "__main__" :
    i : int = int(input("Dijite un número entero: "))
    j : int = int(input("Dijite un número entero: "))

    if j < 0 and i < 0 :
        print("Dijite solamente números positivos")
    else:
        print(f"El número {i} elevado a {j} es igual a {PotenciaRecursiva(i,j)}")
