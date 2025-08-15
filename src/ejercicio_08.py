def impares():
    fib = [0, 1]

    while len(fib) < 20:
        siguiente = fib[-1] + fib[-2]
        fib.append(siguiente)

    tupla = tuple(fib)

    print("Secuencia de Fibonacci:")
    print(tupla)

    print("Números impares en la secuencia:")
    for num in tupla:
        if num % 2 != 0:
            print(num)

impares()
