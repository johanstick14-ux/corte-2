numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))

prom = sum(numeros) / len(numeros)

mayores = []
for n in numeros:
    if n > prom:
        mayores.append(n)

print("Promedio:", prom)
print("Mayores que el promedio:", mayores)