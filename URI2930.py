Z = str(input()).split()

N = int(Z[0])
D = int(Z[1])

if D - N >= 3:
    print('Muito bem! Apresenta antes do Natal!')

elif D - N < 0:
    print('Eu odeio a professora!')

elif D - N <= 2:
    print('Parece o trabalho do meu filho!')

    if N <= 21:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')
