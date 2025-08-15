lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print("Los pares son:", pares(lista))
