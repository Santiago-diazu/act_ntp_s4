def filtrarEstudiantes():
    estudiantes = []

    print("Ingresa los datos de los estudiantes (nombre, edad y promedio). \nPara terminar, escribe 'fin' en el apartado de nombre.")

    while True:
        nombre = input("Nombre: ").strip()
        if nombre.lower() == 'fin':
            break

        try:
            edad = int(input("Edad: "))
            promedio = float(input("Promedio: "))
        except ValueError:
            print("Error: Edad debe ser un número entero y promedio un número decimal.")
            continue

        estudiantes.append((nombre, edad, promedio))

    estudiantes = tuple(estudiantes)

    filtro = []
    for estudiante in estudiantes:
        if estudiante[2] > 8.0:
            filtro.append(estudiante)

    filtro = tuple(filtro)

    print("Estudiantes con promedio mayor a 8.0:")
    if filtro:
        for e in filtro:
            print(e)
    else:
        print("No hay estudiantes con promedio mayor a 8.0.")

filtrarEstudiantes()

