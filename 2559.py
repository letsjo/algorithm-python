# 수열

n, k = map(int,input().split())

temperature = list(map(int,input().split()))

sum = 0
max = -1000000000

for i in range(n):
    sum += temperature[i]
    if i >= k:
        sum -= temperature[i-k]
    if i >= k-1 and sum > max:
        max = sum

print(max)