tipo = input("ingrese el tipo de articulo: ")

if tipo == "textil":
    print("descuento 0%")
elif tipo == "electrodomestico":
    print("descuento 3.7%")
elif tipo == "elementos de cocina":
    print("descuento 4.2%")
elif tipo == "video juego":
    print("descuento 7.8%")
else:
    print("tipo no valido")