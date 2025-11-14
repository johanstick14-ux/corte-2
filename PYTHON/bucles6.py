clave_correcta = "1234"
intentos = 0

while intentos < 3:
    clave = input("Ingrese la clave: ")

    if clave == clave_correcta:
        print("Acceso permitido")
        break

    intentos += 1
    print("Clave incorrecta")

if intentos == 3:
    print("Acceso denegado")