while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 3:
        print("Saliendo...")
        break

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    if opcion == 1:
        print("Resultado:", a + b)
    elif opcion == 2:
        print("Resultado:", a - b)
    else:
        print("Opcion invalida")