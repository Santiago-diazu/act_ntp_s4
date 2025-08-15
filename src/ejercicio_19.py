def calificaciones():
    estudiantes = {}

    while True:
        print("Gestión de Calificaciones: \n1. Agregar estudiante \n2. Agregar calificación a un estudiante \n3. 3. Calcular promedio de un estudiante \n4. Mostrar todos los estudiantes con sus calificaciones \n5. Salir")

        opcion = input("Digita la opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip().capitalize()
            if nombre in estudiantes:
                print("El nombre del estudiante ya existe.")
            else:
                estudiantes[nombre] = []
                print("Estudiante agregado.")

        elif opcion == "2":
            nombre = input("Nombre del estudiante: ").strip().capitalize()
            if nombre in estudiantes:
                try:
                    nota = float(input("Ingresa la calificación: "))
                    estudiantes[nombre].append(nota)
                    print("Se ha agregado la calificación al estudiante.")
                except ValueError:
                    print("La calificación tiene que ser un número.")
            else:
                print("El estudiante ingresado no se encuentra registrado.")

        elif opcion == "3":
            nombre = input("Nombre del estudiante: ").strip().capitalize()
            if nombre in estudiantes:
                calificaciones = estudiantes[nombre]
                if calificaciones:
                    promedio = sum(calificaciones) / len(calificaciones)
                    print(f"El promedio de {nombre} es de {promedio:.2f}")
                else:
                    print("El nombre ingresado no tiene calificaciones.")
            else:
                print("El estudiante ingresado no se encuentra registrado.")

        elif opcion == "4":
            if estudiantes:
                print("La lista de estudiantes y sus calificaciones son:")
                for nombre, notas in estudiantes.items():
                    print(f"{nombre}: {notas if notas else 'no tiene calificaciones registradas'}")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            break

        else:
            print("Ingresa un número del 1 al 5.")

calificaciones()
