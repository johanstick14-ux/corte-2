notas = {}

cant = int(input("¿Cuántos estudiantes? "))

for i in range(cant):
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    notas[nombre] = nota

promedio = sum(notas.values()) / len(notas)

print("Promedio general:", promedio)