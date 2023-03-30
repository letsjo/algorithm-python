# 바구니 뒤집기

N, M = map(int, input().split(' '))

baskets = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split(' '))
    start = j-1
    if (i-2 < 0):
        stop = None
    else:
        stop = i-2
    changeIndex = i-1
    for changeValue in baskets[start:stop:-1]:
        baskets[changeIndex] = changeValue
        changeIndex += 1

print(' '.join(baskets))
