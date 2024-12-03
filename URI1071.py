soma = n1 = n2 = 0
x = int(input())
y = int(input())

if x < y:
    n1 = x
    n2 = y

if y <= x:
    n1 = y
    n2 = x

for c in range(n1+1, n2):
    if c % 2 != 0:
        soma += c

print(soma)
