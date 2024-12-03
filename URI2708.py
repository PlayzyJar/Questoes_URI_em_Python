jipe = pessoas = 0

while True:
    line = str(input()).split()

    if str(line[0]) == 'ABEND':
        break

    elif str(line[0]) == 'SALIDA':
        jipe += 1
        pessoas += int(line[1])

    elif str(line[0]) == 'VUELTA':
        jipe -= 1
        pessoas -= int(line[1])

print(pessoas)
print(jipe)
