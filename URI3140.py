html = []
linha = str(input())
c = 1
while linha.strip() != '</html>':

    html.append(linha)
    linha = str(input())

for cont, line in enumerate(html):

    if line.strip() == '<body>':
        c = cont + 1
        while html[c].strip() != '</body>':
            c += 1
        break
