agenda = {}

while True:
    nombre = input("Nombre (fin para terminar): ")

    if nombre == "fin":
        break

    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print(agenda)