import math
i = int(input("ingrese el radio -> "))
##es hallar la superficie y el perimetro 
s = math.pi * float(i**2)
p = 2 * math.pi * float(i)

print(f"la superficie es {s} y el perimetro es {p}")