print("--- Verificacion de Multiples Rangos (3.5, 7.8] O [23.4, 45.3] ---")

x = float(input("Ingrese el numero: "))

con1 = (x > 3.5 and x <= 7.8)

con2 = (x >= 23.4 and x <= 45.3)

if con1 or con2:
    print(f" El numero {x} si pertenece a al menos uno de los rangos.")
else:
    print(f" El numero {x} no pertenece a ninguno de los rangos.")