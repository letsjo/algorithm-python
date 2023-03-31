# 행렬 덧셈

N, M = map(int, input().split())
A = [[] for _ in range(N)]
B = [[] for _ in range(N)]


def createList(arr):
    for i in range(N):
        for value in list(map(int, input().split())):
            arr[i].append(value)
    return arr


A = createList(A)
B = createList(B)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()
