numero1 = int(input("Introduce el primer numero entero: "))
numero2 = int(input("Introduce el segundo numero entero: "))

if numero1 > numero2:
    print(f"El mayor numero es: {numero1}")
elif numero2 > numero1:
    print(f"El mayor numero es: {numero2}")
else:
    print("Ambos numeros son iguales.")