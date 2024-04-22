def factorialRecursivo(n : int )-> int:
  print(n)
  # Caso base 
  if n == 1: 
    return 1
  else:
    # Condicion de la funcion recursiva
    return n*factorialRecursivo(n-1)

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  factorialDeNum = factorialRecursivo(num)
  print("El factorial de " + str(num) + " es " + str(factorialDeNum))