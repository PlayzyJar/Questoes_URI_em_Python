n = int(input())
c = r = s = 0

for i in range(1, n + 1):
    x = str(input()).split()
    a = int(x[0])
    b = str(x[1])

    if b == 'C':
        c += a
    if b == 'R':
        r += a
    if b == 'S':
        s += a

total = c + r + s

pc = (c / total) * 100
pr = (r / total) * 100
ps = (s / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')
