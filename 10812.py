# 바구니 순서 바꾸기

N, M = map(int, input().split())

baskets = [str(i+1) for i in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    index = i-1
    originBaskets = baskets.copy()
    for value in originBaskets[k-1:j]:
        baskets[index] = value
        index += 1
    for value in originBaskets[i-1:k-1]:
        baskets[index] = value
        index += 1

print(' '.join(baskets))
