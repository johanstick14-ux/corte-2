x = int(input("ingresa un numero: "))

print("ingresa el primer intervalo")
a1 = int(input("limite 1: "))
b1 = int(input("limite 2: "))

print("ingresa el segundo intervalo")
a2 = int(input("limite 1: "))
b2 = int(input("limite 2: "))

print("ingresa el tercer intervalo")
a3 = int(input("limite 1: "))
b3 = int(input("limite 2: "))

dentro1 = x > a1 and x < b1
dentro2 = x > a2 and x < b2
dentro3 = x > a3 and x < b3

if dentro1 or dentro2 or dentro3:
    print("x esta dentro de uno de los intervalos")
else:
    print("x esta fuera de todos los intervalos")