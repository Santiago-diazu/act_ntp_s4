carrito = []
precios = {}

while True:
    print("Menú Carrito de Compras")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Calcular total")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
            producto = input("Nombre del producto a agregar: ").strip()
            try:
                precio = float(input(f"Precio de '{producto}': "))
            except ValueError:
                print("Precio inválido. Intenta de nuevo.")
                continue

            carrito.append(producto)
            precios[producto] = precio
            print(f"Producto '{producto}' agregado al carrito.")

    elif opcion == '2':
            if not carrito:
                print("El carrito está vacío.")
                continue

            producto = input("Nombre del producto a eliminar: ").strip()
            if producto in carrito:
                carrito.remove(producto)
                precios.pop(producto, None)
                print(f"Producto '{producto}' eliminado del carrito.")
            else:
                print(f"El producto '{producto}' no está en el carrito.")

    elif opcion == '3':
            if not carrito:
                print("El carrito está vacío.")
            else:
                print("Productos en el carrito:")
                for prod in carrito:
                    print(f"- {prod}: ${precios[prod]:.2f}")

    elif opcion == '4':
            if not carrito:
                print("El carrito está vacío.")
            else:
                total = sum(precios[prod] for prod in carrito)
                print(f"Total a pagar: ${total:.2f}")

    elif opcion == '5':
            print("Gracias por usar el carrito de compras.")
            break

    else:
            print("Opción no válida. Intenta de nuevo.")
