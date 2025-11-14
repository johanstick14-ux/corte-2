N = int(input("Ingrese N: "))
M = int(input("Ingrese M: "))

encontrado = False

for i in range(N, M + 1):
    if i % 9 == 0:
        print("Primer multiplo de 9:", i)
        encontrado = True
        break

if not encontrado:
    print("No hay multiplos de 9 en el rango")