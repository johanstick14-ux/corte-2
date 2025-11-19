frase = input("Ingrese una frase: ")

palabras = frase.split()
contador = {}

for p in palabras:
    if p in contador:
        contador[p] += 1
    else:
        contador[p] = 1

print(contador)