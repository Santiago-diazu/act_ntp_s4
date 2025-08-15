def suma():
    lista1 = input("Ingresa los elementos de la primera tupla separados por comas. \nTupla 1: ")
    lista2 = input("Ingresa los elementos de la segunda tupla separados por comas. \nTupla 2: ")

    try:
        tupla1 = tuple(int(x.strip()) for x in lista1.split(','))
        tupla2 = tuple(int(x.strip()) for x in lista2.split(','))
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por comas.")
        return

    if len(tupla1) != len(tupla2):
        print("Error: Las tuplas deben tener la misma longitud.")
        return

    resultado = []
    for i in range(len(tupla1)):
        suma = tupla1[i] + tupla2[i]
        resultado.append(suma)

    resultadoTupla = tuple(resultado)
    print("Resultado de la suma:", resultadoTupla)

suma()

