N = int(input())
h = N // 3600
res = N - (h*3600)
minu = res // 60
res -= (minu*60)
print(f'{int(h)}:{int(minu)}:{int(res)}')
