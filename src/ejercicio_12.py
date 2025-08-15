def palabras():
    unicas = set()
    repetidas = set()

    print("Ingresa una palabra. Escriba 'salir' para terminar.")

    while True:
        palabra = input("Palabra: ").strip().lower()

        if palabra == "salir":
            break

        if palabra in unicas:
            repetidas.add(palabra)
        else:
            unicas.add(palabra)

    final = unicas - repetidas

    print(f"Número de palabras únicas ingresadas: {len(final)}")
    print("Palabras repetidas:", repetidas)

palabras()
