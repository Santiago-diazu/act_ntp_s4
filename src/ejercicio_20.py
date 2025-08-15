def temperaturasRegistro():
    temperaturas = {}

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    while True:
        print("Registro de Temperaturas: \n1. Agregar/Actualizar temperatura \n2. Mostrar estadísticas por ciudad \n3. Mostrar temperaturas por día \n4. Mostrar todo el registro \n5. Salir")

        opcion = input("Digita la opción (1-5): ")

        if opcion == "1":
            ciudad = input("Ingresa el nombre de la ciudad: ").strip().capitalize()
            dia = input("Ingresa el día de la semana: ").strip().capitalize()

            if dia not in dias_semana:
                print("El día ingresado no pertenece a un día de la semana.")
                continue

            try:
                temp = float(input("Temperatura registrada (°C): "))
            except ValueError:
                print("La temperatura ingresada no es válida.")
                continue

            if ciudad not in temperaturas:
                temperaturas[ciudad] = {}
            temperaturas[ciudad][dia] = temp
            print("La temperatura fue registrada.")

        elif opcion == "2":
            ciudad = input("Ingresa el nombre de la ciudad a consultar: ").strip().capitalize()
            if ciudad in temperaturas:
                datos = temperaturas[ciudad]
                if datos:
                    valores = list(datos.values())
                    promedio = sum(valores) / len(valores)
                    maxima = max(valores)
                    minima = min(valores)
                    print(f"La estadísticas de {ciudad} es: \nEl promedio es: {promedio:.2f}°C \nLa máxima es: {maxima}°C \nLa mínima es: {minima}°C")

                else:
                    print("No hay datos registrados para la ciudad ingresada.")
            else:
                print("La ciudad no se encuentra registrada..")

        elif opcion == "3":
            dia = input("Ingresa el día a consultar: ").strip().capitalize()
            if dia not in dias_semana:
                print("El día ingresado no se encuentra.")
                continue

            print(f"Temperaturas registradas el {dia}:")
            encontrado = False
            for ciudad, dias in temperaturas.items():
                if dia in dias:
                    print(f"{ciudad}: {dias[dia]}°C")
                    encontrado = True
            if not encontrado:
                print("No hay datos registrados para el día ingresado.")

        elif opcion == "4":
            if temperaturas:
                print("El registro completo de temperaturas es:")
                for ciudad, dias in temperaturas.items():
                    print(f"{ciudad}:")
                    for dia, temp in dias.items():
                        print(f"  {dia}: {temp}°C")
            else:
                print("No hay datos registrados.")

        elif opcion == "5":
            break

        else:
            print("Ingresa un número del 1 al 5.")


temperaturasRegistro()