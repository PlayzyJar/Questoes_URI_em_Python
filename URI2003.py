ok = True
while ok:

    try:
        horasenter = str(input()).split(':')

        hora = int(horasenter[0]) + 1
        minutos = int(horasenter[1])

        if hora - 8 < 0:
            print('Atraso maximo: 0')

        else:
            minutos += (hora - 8) * 60
            print(f'Atraso maximo: {minutos}')

    except:
        ok = False
