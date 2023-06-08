# ATM

n = int(input())
p = list(map(int, input().split()))

# p.sort()
# insert sort
for i in range(1, n):
    key = p[i]
    j = i - 1
    while j >= 0 and p[j] > key:
        p[j + 1] = p[j]
        j -= 1
    p[j + 1] = key

sum = 0
for i in range(n):
    sum += p[i] * (n - i)

print(sum)