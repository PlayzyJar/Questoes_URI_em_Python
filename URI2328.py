N = int(input())
Estoque = 0
cortes = []
corteatual = str(input()).split()

for c in range(0, N):
    cortes.append(int(corteatual[c])-1)

print(sum(cortes))
