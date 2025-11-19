nivel = float(input("ingresa el nivel del tanque en litros: "))

if nivel < 250:
    print("abrir")
elif nivel > 450:
    print("cerrar")
else:
    print("mantener igual")