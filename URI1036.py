D = str(input()).split()
A = float(D[0])
B = float(D[1])
C = float(D[2])

Delta = B * B - 4 * A * C

if Delta < 0 or A == 0:
    print('Impossivel calcular')

else:
    x1 = (-B + (Delta**0.5)) / (2*A)
    x2 = (-B - (Delta**0.5)) / (2*A)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
