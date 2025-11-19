x, y = map(int, input("Ingrese x y y separados por espacio: ").split())
tupla = (x, y)

limite1 = 0
limite2 = 10

if limite1 <= tupla[0] <= limite2 and limite1 <= tupla[1] <= limite2:
    print("Dentro del rango")
else:
    print("Fuera del rango")