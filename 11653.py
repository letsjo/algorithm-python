# 소인수분해

N = int(input())
answer = []

for i in range(2, N+1):
    while N % i == 0:
        N /= i
        print(i)
    if N == 1:
        break
