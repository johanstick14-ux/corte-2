def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    a = float(input("ingrese a: "))
    b = float(input("ingrese b: "))
    op = input("operacion (+, -, *, /): ")

    if op == "+":
        return sumar(a, b)
    elif op == "-":
        return restar(a, b)
    elif op == "*":
        return multiplicar(a, b)
    elif op == "/":
        return dividir(a, b)
    else:
        return "operacion no valida"