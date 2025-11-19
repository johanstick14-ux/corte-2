tipo = int(input("Ingrese el tipo de articulo (1, 2, 3 u otro): "))
precio = float(input("Ingrese el precio del articulo: "))

if tipo == 1:
    descuento = 0.125
elif tipo == 2:
    descuento = 0.083
elif tipo == 3:
    descuento = 0.032
else:
    descuento = 0.0

valor_descuento = precio * descuento
precio_final = precio - valor_descuento

print("Descuento aplicado:", valor_descuento)
print("Precio final:", precio_final)