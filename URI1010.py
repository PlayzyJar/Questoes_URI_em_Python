p1 = str(input()).split()
p2 = str(input()).split()

val1 = int(p1[1]) * float(p1[2])
val2 = int(p2[1]) * float(p2[2])

print(f'VALOR A PAGAR: R$ {val1 + val2:.2f}')
