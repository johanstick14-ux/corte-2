def potencia(base, exponente):
    resultado = 1
    i = 1
    while i <= exponente:
        resultado = resultado * base
        i = i + 1
    return resultado