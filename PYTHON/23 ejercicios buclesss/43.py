numero = int(input("Ingrese un numero entero: "))

if numero > 0:
    texto = str(numero)
    cifras = len(texto)

    suma = 0
    i = 0

    while i < cifras:
        suma = suma + int(texto[i])
        i = i + 1

    print("Cantidad de cifras:", cifras)
    print("Suma de las cifras:", suma)
else:
    print("El numero no es positivo")