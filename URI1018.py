valor = total = int(input())
print(valor)
cedulas = 0

cedulaatual = [100, 50, 20, 10, 5, 2, 1]
qtdcedulas = [0, 0, 0, 0, 0, 0, 0]
cont = 0
while True:
    if total > 0:
        qtdcedulas[cont] = total // cedulaatual[cont]
        total -= qtdcedulas[cont] * cedulaatual[cont]
        cont += 1

    else:
        cont = 0
        break

for c in qtdcedulas:
    print(f'{c} nota(s) de R$ {cedulaatual[cont]},00')
    cont += 1
