n = int(input("ingresa un numero: "))

for x in range(0, n + 1, 2):
    f = x**3 + x**2 - 5
    print("x =", x, "f(x) =", f)