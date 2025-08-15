def buscarLetra():
    listaPalabras = []

    print("Ingresa la palabra que desees ingresar en la lista. Escribe 'fin' para terminar.")    

    while True:

        palabra = input("Palabra: ").strip()
        if palabra.lower() == 'fin':
            break
        listaPalabras.append(palabra)

    letra = input("Ingresa la letra para buscar: ").lower()
    resultado = []

    for palabra in listaPalabras:
        for caracter in palabra:
            if caracter.lower() == letra:
                resultado.append(palabra)
                break  

    if resultado:
        print("Palabras que contienen la letra '{}':".format(letra))
        for palabra in resultado:
            print("-", palabra)
    else:
        print("Ninguna palabra contiene la letra '{}'.".format(letra))

buscarLetra()

