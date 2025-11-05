cantidad = int(input("Ingrese la cantidad de dinero: "))
porcentajeIntereses = float(input("Ingrese el porcentaje de intereses: "))
periodos = int(input("Ingrese la cantidad de periodos: "))

porcentaje = porcentajeIntereses / 100
valorIntereses = cantidad * porcentaje * periodos
print(f"El valor de los intereses es: {valorIntereses}")
impuesto = valorIntereses * 0.7
print(f"El valor del impuesto es: {impuesto}")

total = cantidad + valorIntereses - impuesto
print(f"El valor total es: {total}")
