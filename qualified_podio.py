def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    lista_tempos = []

    lista_tempos.append(tempo_chegada2)
    lista_tempos.append(tempo_chegada1)
    lista_tempos.append(tempo_chegada3)
    lista_tempos.sort()
    return print("1 - {} minutos\n2 - {} minutos\n3 - {} minutos".format(lista_tempos[0],lista_tempos[1],lista_tempos[2]))

podio_olimpico(1,9,7)

