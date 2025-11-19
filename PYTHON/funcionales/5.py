A = [[1, 2, 3], [4, 5, 6]]

filas = len(A)
columnas = len(A[0])

transpuesta = []

for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(A[i][j])
    transpuesta.append(fila)

print(transpuesta)