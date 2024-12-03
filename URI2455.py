PeC = str(input()).split()

P1 = int(PeC[0])
C1 = int(PeC[1])
P2 = int(PeC[2])
C2 = int(PeC[3])

if P1 * C1 == P2 * C2:
    print('0')
if P1 * C1 > P2 * C2:
    print('-1')
if P1 * C1 < P2 * C2:
    print('1')
