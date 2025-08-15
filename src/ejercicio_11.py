def conjuntos():
    entrada1 = input("Ingresa los elementos de la primera lista, separados por comas. \nLista 1: ")
    entrada2 = input("Ingresa los elementos de la segunda lista, separados por comas. \nLista 2: ")

    lista1 = [x.strip() for x in entrada1.split(',')]
    lista2 = [x.strip() for x in entrada2.split(',')]

    conjunto1 = set()
    for elemento in lista1:
        conjunto1.add(elemento)

    conjunto2 = set()
    for elemento in lista2:
        conjunto2.add(elemento)

    union = conjunto1 | conjunto2
    interseccion = conjunto1 & conjunto2
    diferencia = conjunto1 - conjunto2
    diferenciaSimetrica = conjunto1 ^ conjunto2

    print("\nConjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia:", diferencia)
    print("Diferencia simétrica:", diferenciaSimetrica)

conjuntos()
