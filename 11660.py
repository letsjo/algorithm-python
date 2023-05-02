# 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
sumList = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N):
    arr.append(list(map(int, input().split())))

sumList[1][1] = arr[0][0]

# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

# [0,0,0,0,0]
# [0,1,3,6,10]
# [0,3,9,9,14]
# [0,6,19,19,37]
# [0,10,34,37,81]

x = 0
y = 0
for i in range(1, N+1):
    x += arr[i-1][0]
    y += arr[0][i-1]
    sumList[i][1] = x
    sumList[1][i] = y

for i in range(1, N):
    for j in range(1, N):
        sumList[i+1][j+1] = sumList[i+1][j] + \
            sumList[i][j+1] + arr[i][j] - sumList[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumList[x2][y2] - sumList[x2][y1-1] -
          sumList[x1-1][y2] + sumList[x1-1][y1-1])
