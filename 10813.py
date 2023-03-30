# 공 바꾸기

N, M = map(int, input().split(' '))
baskets = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split(' '))
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(' '.join(baskets))
