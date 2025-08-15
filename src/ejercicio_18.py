def agenda():
    agenda = {}

    while True:
        print("Menú de agenda telefónica. \n1. Agregar contacto \n2. Buscar contacto por nombre \n3. Mostrar todos los contactos \n4. Eliminar contacto \n5. Salir")

        opcion = input("Digita la opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ").strip().capitalize()
            if nombre in agenda:
                print("Ese contacto ya existe.")
            else:
                numero = input("Número de teléfono: ").strip()
                agenda[nombre] = numero
                print("El contacto ha sido agregado")

        elif opcion == "2":
            nombre = input("Nombre a buscar: ").strip().capitalize()
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print("El nombre ingresado no se encuentra registrado en la agenda")

        elif opcion == "3":
            if agenda:
                print("Los contactos ingresado en la agenda son:")
                for nombre, numero in agenda.items():
                    print(f"- {nombre}: {numero}")
            else:
                print("La agenda no tiene contactos ingresados.")

        elif opcion == "4":
            nombre = input("Nombre el nombre del contacto que se va a eliminar: ").strip().capitalize()
            if nombre in agenda:
                del agenda[nombre]
                print("El contacto ha sido eliminado.")
            else:
                print("El contacto no se encuentra en la egenda.")

        elif opcion == "5":
            break

        else:
            print("Ingresa un número del 1 al 5.")

agenda()
