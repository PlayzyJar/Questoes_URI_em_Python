E = str(input()).split()
A = int(E[0])
B = int(E[1])
C = int(E[2])
D = int(E[3])

CD = C + D
AB = A + B
if B > C and D > A and CD > AB and C >= 0 and D >= 0 and A % 2 == 0:
    print('Valores aceitos')

else:
    print('Valores não aceitos')
