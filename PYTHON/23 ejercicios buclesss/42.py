cantidad = int(input("ingrese la cantidad de estudiantes: "))

aprobados = 0
reprobados = 0
suma_notas = 0

contador = 1

while contador <= cantidad:
    codigo = input("ingrese el código del estudiante: ")
    nota = float(input("ingrese la nota del estudiante: "))

    suma_notas = suma_notas + nota

    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    contador = contador + 1

promedio = suma_notas / cantidad

print("aprobados:", aprobados)
print("reprobados:", reprobados)
print("promedio del grupo:", promedio)