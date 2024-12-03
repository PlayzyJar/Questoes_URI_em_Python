cpf = list()
dinheiro1 = list()
cod1 = str(input())
cod2 = str(input())
cont = ponto = ok = 0
nums1 = list()
nums2 = list()
n1 = ''
n2 = ''

for c in cod1:
    if ponto == 0:
        if c.isnumeric():
            nums1.append(str(c))
        elif c == '.':
            nums1.append(str(c))
            ponto = 1

    if '.' in nums1:
        if ponto == 3:
            break

        if c.isnumeric() and c != '.' and ok == 0:
            if c.isnumeric() and c != '.':
                nums1.append(str(c))
                ponto += 1
            elif c == '.':
                ok += 1

cpf = nums1[:11]
dinheiro1 = nums1[11:]

for cont in dinheiro1:
    n1 += cont
if '.' in n1:
    n1 = float(n1)
else:
    n1 = int(n1)

ponto = ok = 0

for v in cod2:
    if ponto == 0:
        if v.isnumeric():
            nums2.append(str(v))

        if v == '.':
            nums2.append(str(v))
            ponto = 1

    if '.' in nums2:
        if ponto == 3:
            break

        if v.isnumeric() and v != '.':
            if v.isnumeric() and v != '.' and ok == 0:
                nums2.append(str(v))
                ponto += 1
            elif v == '.':
                ok += 1

for pos in nums2:
    n2 += pos

if '.' in n2:
    n2 = float(n2)
else:
    n2 = int(n2)

print('cpf ', end='')
for numero in cpf:
    print(f'{numero}', end='')
print(f'\n{n1+n2:.2f}')
