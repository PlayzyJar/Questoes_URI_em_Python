Diasenter = total = int(input())
Dias = [365, 30, 1]
Tempos = [0, 0, 0]
cont = 0
while total > 0:
    if total >= Dias[cont]:
        total -= Dias[cont]
        Tempos[cont] += 1

    else:
        cont += 1

print(f'{Tempos[0]} ano(s) \n{Tempos[1]} mes(es)')
print(f'{Tempos[2]} dia(s)')