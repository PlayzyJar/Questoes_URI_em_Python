from math import sqrt

p1 = str(input()).split()
p2 = str(input()).split()

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'{d:.4f}')
