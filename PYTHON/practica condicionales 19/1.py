costo = float(input("ingresa el costo del articulo: "))

if costo > 150000:
    descuento = costo * 0.05
else:
    descuento = 0

print("el descuento es:", descuento)