lista = input("Ingrese elementos separados por espacio: ").split()

sin_repetidos = tuple(set(lista))

print(sin_repetidos)