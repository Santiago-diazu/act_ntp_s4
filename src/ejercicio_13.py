def conjuntos():
    pares = set()
    multiplo3 = set()


    for i in range(2, 21):
        if i % 2 == 0:
            pares.add(i)

    for i in range(3, 31):
        if i % 3 == 0:
            multiplo3.add(i)

    print("Conjunto 1:", pares)
    print("Conjunto 2:", multiplo3)

    union = pares | multiplo3
    interseccion = pares & multiplo3
    diferencia = pares - multiplo3
    simetrica = pares ^ multiplo3

    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia:", diferencia)
    print("Diferencia simétrica:", simetrica)

conjuntos()
