n1 = float(input("ingresa la nota 1: "))
n2 = float(input("ingresa la nota 2: "))
n3 = float(input("ingresa la nota 3: "))
n4 = float(input("ingresa la nota 4: "))
n5 = float(input("ingresa la nota 5: "))

definitiva = (n1 + n2 + n3 + n4 + n5) / 5

print("nota definitiva:", definitiva)

if definitiva > 3.5:
    print("gano el curso")
else:
    print("perdio el curso")