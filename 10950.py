# A+B - 3

N = int(input())
result = ''
for i in range(N):
    a, b = map(int, input().split())
    result += str(a + b) + ('\n' if N != i+1 else '')

print(result)
