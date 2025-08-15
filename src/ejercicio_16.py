def inventario_productos():
    inventario = {}

    while True:
        print("Menú de Inventario: \n1. Agregar producto. \n2. Actualizar. \n3. Eliminar producto. \n4. Mostrar inventario. \n5. Salir.")

        opcion = input("Digita la opción (1-5): ")

        if opcion == "1":
            producto = input("Nombre del producto a agregar: ").strip().capitalize()
            if producto in inventario:
                print("El producto ya existe en el inventario.")
            else:
                try:
                    cantidad = int(input("Cantidad: "))
                    inventario[producto] = cantidad
                    print(f"Producto '{producto}' agregado con cantidad {cantidad}.")
                except ValueError:
                    print("Por favor ingresa un número válido.")

        elif opcion == "2":
            producto = input("Nombre del producto a actualizar: ").strip().capitalize()
            if producto in inventario:
                try:
                    cantidadNueva = int(input("Nueva cantidad: "))
                    inventario[producto] = cantidadNueva
                    print(f"El producto '{producto}' quedó actualizado a {cantidadNueva}.")
                except ValueError:
                    print("Por favor ingresa un número válido.")
            else:
                print("Ese producto no existe en el inventario.")

        elif opcion == "3":
            producto = input("Nombre del producto a eliminar: ").strip().capitalize()
            if producto in inventario:
                del inventario[producto]
                print(f"El producto '{producto}' ha sido eliminado del inventario.")
            else:
                print("Ese producto no se encuentra.")

        elif opcion == "4":
            if inventario:
                print("Inventario actual:")
                for prod, cant in inventario.items():
                    print(f"- {prod}: {cant}")
            else:
                print("El inventario está vacío.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Ingresa un número del 1 al 5.")
