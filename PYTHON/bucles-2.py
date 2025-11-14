N = int(input("ingrese un numero: "))

a = 0
b = 1

while a <= N:
    print(a)
    c = a + b
    a = b
    b = c