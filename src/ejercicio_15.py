def conjunto():
    entrada = input("Ingrese lista de números separados por coma. ")

    try:
        listaIngresada = [int(x.strip()) for x in entrada.split(',')]
    except ValueError:
        print("Asegurese a ingresar los número separados por coma.")
        return

    listaFiltrada = set()

    for numero in listaIngresada:
        listaFiltrada.add(numero)

    listaOriginal = len(listaIngresada)
    listaFinal = len(listaFiltrada)
    duplicados = listaOriginal - listaFinal

    print("Lista original:", listaIngresada, "\nNúmeros únicos:", listaFiltrada, f"Cantidad de duplicados encontrados: {duplicados}" )

conjunto()
