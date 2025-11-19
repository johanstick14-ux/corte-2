a = float(input("ingresa a: "))
b = float(input("ingresa b: "))
c = float(input("ingresa c: "))

discriminante = b*b - 4*a*c

if a != 0 and discriminante >= 0:
    print("la ecuacion tiene solucion")
else:
    print("la ecuacion no tiene solucion")
