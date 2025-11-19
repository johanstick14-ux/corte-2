n = int(input("digita un numero: "))

if n < 0:
    print("los numeros negativos no tienen factorial")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i

    print("el factorial de", n, "es:", factorial)