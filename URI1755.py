ppA = int(input('>>Informe a população da cidade A: '))
while ppA < 0:
    print('\033[1;31m>>Erro! O número da população deve ser inteiro e positivo.\033[m')
    ppA = int(input('>>Por favor, tente novamente: '))

icA = float(input('>>Informe o índice de crescimento anual da cidade A: '))
while icA < 0:
    print('\033[1;31m>>Erro! O índice de crescimento anual deve ser positivo.\033[m')
    icA = float(input('>>Por favor, tente novamente: '))

ppB = int(input('>>Informe a população da cidade B: '))
while ppB < 0:
    print('\033[1;31m>>Erro! O número da população deve ser inteiro e positivo.\033[m')
    ppB = int(input('>>Por favor, tente novamente: '))

icB = float(input('>>Informe o índice de crescimento anual da cidade B: '))
while icB < 0:
    print('\033[1;31m>>Erro! O índice de crescimento anual deve ser positivo.\033[m')
    icB = float(input('>>Por favor, tente novamente: '))

ano = int(input('>>Informe o ano atual: '))
while ano > 9999 or ano < 1900:
    ano = int(input('>>Erro! Ano inválido, tente novamente: '))

cont = 0
while ppA > ppB:
    if cont == 1000:
        break
    ano += 1
    cont += 1
    ppA += icA/100
    ppB += icB/100

if cont < 1000:
    print(f'>>No ano {ano}, a cidade B ultrapassará a cidade A em habitantes.')
    print(f'>>População da cidade A: {ppA}')
    print(f'>>População da cidade B: {ppB}')

elif ppB < ppA and icA > icB:
    print('A população da cidade B nunca ultrapassará a da cidade A. Pois o índice')
    print('de crescimento e a população da cidade B é menor que o da cidade A.')
