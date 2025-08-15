def frecuencia():
    frase = input("Ingresa la frase a analizar.")
    palabras = frase.lower().split()

    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    orden = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    print("\nFrecuencia de palabras (de mayor a menor):")
    for palabra, frecuencia in orden:
        print(f"{palabra}: {frecuencia}")

frecuencia()