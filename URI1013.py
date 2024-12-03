d = str(input()).split()
a = int(d[0])
b = int(d[1])
c = int(d[2])

maior = a

if b >= a:
    maior = b

if c >= maior:
    maior = c

print(f'{maior} eh o maior')
