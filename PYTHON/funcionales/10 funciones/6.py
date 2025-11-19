def contar_digitos(n):
    if n == 0:
        return 1

    n = abs(n)
    conteo = 0

    while n > 0:
        conteo = conteo + 1
        n = n // 10

    return conteo