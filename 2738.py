# 행렬 덧셈

N, M = map(int, input().split())
A = [[] for _ in range(N)]

for i in range(N):
    for value in list(map(int, input().split())):
        A[i].append(value)

for i in range(N):
    j = 0
    for value in list(map(int, input().split())):
        print(A[i][j]+value, end=' ')
        j += 1
    print()
