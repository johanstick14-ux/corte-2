android = 0
ios = 0

cantidad = int(input("cuantos estudiantes van a votar: "))

for i in range(cantidad):
    codigo = input("digita tu codigo: ")
    eleccion = input("digita tu plataforma (android o ios): ")

    if eleccion == "android":
        android = android + 1
    elif eleccion == "ios":
        ios = ios + 1
    else:
        print("plataforma no valida, tu voto no cuenta")

print("votos android:", android)
print("votos ios:", ios)

if android > ios:
    print("gana android")
elif ios > android:
    print("gana ios")
else:
    print("hay empate, se usara otro metodo de eleccion")