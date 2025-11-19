tabla = int(input("ingresa la tabla que quieres repasar (1 a 20): "))

aciertos = 0

for i in range(1, 11):
    print("cuanto es", tabla, "x", i, "?")
    r = int(input("respuesta: "))
    
    if r == tabla * i:
        print("muy bien, correcto")
        aciertos = aciertos + 1
    else:
        print("incorrecto, la respuesta era", tabla * i)

print("aciertos:", aciertos)

if aciertos <= 5:
    print("valoracion: insuficiente")
elif aciertos <= 7:
    print("valoracion: aceptable")
elif aciertos <= 9:
    print("valoracion: sobresaliente")
else:
    print("valoracion: excelente")