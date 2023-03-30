# 공 넣기

N, M = map(int, input().split(' '))
baskets = ['0' for i in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split(' '))
    for number in range(i-1, j):
        baskets[number] = str(k)

print(' '.join(baskets))
