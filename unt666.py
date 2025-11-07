sexo = input("Sexo (M mujer / H hombre): ").upper()
edad = int(input("Edad: "))
estatura = float(input("Estatura en metros: "))
soltero = input("¿Es soltero/a?: ").upper()

if soltero == "S":
    if (sexo == "M" and estatura > 1.60 and 20 <= edad <= 25) or \
       (sexo == "H" and estatura > 1.65 and 18 <= edad <= 24):
        print("El aspirante es APTO.")
    else:
        print("El aspirante NO es apto.")
else:
    print("Debe ser soltero/a para poder ingresar.")