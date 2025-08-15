import math

def distanciaTotal():
    puntos = []

    print("Ingresa los puntos (x, y). Para terminar escribe 'fin' en x.")

    while True:
        puntoX = input("x: ").strip()
        if puntoX.lower() == 'fin':
            break

        puntoY = input("y: ").strip()

        try:
            x = float(puntoX)
            y = float(puntoY)
        except ValueError:
            print("Error: x e y deben ser números.")
            continue

        puntos.append((x, y))

    if len(puntos) < 2:
        print("Se necesitan al menos dos puntos para calcular la distancia.")
        return

    distancia = 0.0
    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distancia += d

    print(f"\nDistancia total recorrida: {distancia:.2f}")

distanciaTotal()
