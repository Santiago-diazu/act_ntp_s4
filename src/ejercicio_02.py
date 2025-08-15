def sumaCalificaciones():
    calificaciones = []

    while True:
        entrada = input("Ingresa la calificación. Escribe 'fin' para terminar. ")
        
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            calificaciones.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido o 'fin' para salir.")

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        maxima = max(calificaciones)
        minima = min(calificaciones)

        print(f"Promedio: {promedio:.2f}")
        print(f"Nota más alta: {maxima}")
        print(f"Nota más baja: {minima}")
    else:
        print("No se ingresaron calificaciones.")

sumaCalificaciones()
