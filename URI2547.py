while True:
    try:
        Z = str(input()).split()

        qtd = int(Z[0])
        altmin = int(Z[1])
        altmax = int(Z[2])

        cont = 0

        for c in range(0, qtd):
            altura = int(input())

            if altmin <= altura <= altmax:
                cont += 1
        print(cont)
    except EOFError:
        break
