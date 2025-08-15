def votaciones():

    votos = set()

    while True:
        voto = input("Vota por alguno de los siguientes candidatos: Ana, Luis, Marta, Diego \nEscribe 'fin' para terminar. \n").strip().lower()
        if voto.lower() == 'fin':
            break

        votos.add(voto)

    print("Candidatos que recibieron votos:")
    if votos:
        for candidato in votos:
            print("-", candidato)
    else:
        print("No se registraron votos.")

votaciones()

