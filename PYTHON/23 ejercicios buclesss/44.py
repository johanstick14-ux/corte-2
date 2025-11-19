numero = int(input("ingrese un numero positivo: "))

if numero > 0:
    texto = str(numero)
    cifras = len(texto)

    suma = 0
    i = 0

    while i < cifras:
        digito = int(texto[i])
        suma = suma + (digito ** cifras)
        i = i + 1

    if suma == numero:
        print("es un numero de armstrong")
    else:
        print("no es un numero de armstrong")
else:
    print("el numero no es positivo")