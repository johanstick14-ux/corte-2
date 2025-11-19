nota = float(input("Ingrese la nota del estudiante (0.0 - 5.0): "))

if nota < 3.0:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4.0:
    print("Sobresaliente")
elif nota <= 5.0:
    print("Excelente")
else:
    print("Nota fuera del rango (0.0 - 5.0)")