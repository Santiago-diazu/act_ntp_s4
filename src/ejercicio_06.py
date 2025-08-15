import random
import math

def puntosCirculo():
    puntos = []

    for i in range(10):
        x = random.uniform(-10, 10) 
        y = random.uniform(-10, 10)
        puntos.append((x, y))

    print("Puntos generados:")
    for punto in puntos:
        print(f"{punto}")

    dentroCirculo = []

    for x, y in puntos:
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 5:
            dentroCirculo.append((x, y))

    print("Puntos dentro del círculo de radio 5:")
    for punto in dentroCirculo:
        print(f"{punto}")

puntosCirculo()
