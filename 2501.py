# 약수 구하기

N, K = map(int, input().split())
count = 0

for i in range(1, N+1):
    if (N % i == 0):
        count += 1
        if (count == K):
            break

print(i if count == K else 0)
