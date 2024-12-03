D = str(input()).split()
A = float(D[0])
B = float(D[1])
C = float(D[2])
pi = 3.14159

areatri = (A * C) / 2
areacir = pi * C**2
areatra = ((A+B) * C) / 2
areaqua = B*B
areare = A * B

print(f'TRIANGULO: {areatri:.3f}')
print(f'CIRCULO: {areacir:.3f}')
print(f'TRAPEZIO: {areatra:.3f}')
print(f'QUADRADO: {areaqua:.3f}')
print(f'RETANGULO: {areare:.3f}')
