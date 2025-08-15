lista1 = input("Ingresa la primera lista: ")
lista2 = input("Ingresa la segunda lista: ")

resultado = []
for i in range(len(lista1)):
    resultado.append(lista1[i])
    resultado.append(lista2[i])

print(resultado)