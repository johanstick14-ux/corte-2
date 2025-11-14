n = int(input("Ingrese un numero: "))

for i in range(n, 0, -1):
    print(i)
    if i % 7 == 0:
        print("¡Alerta! multiplo de 7")

print(0)