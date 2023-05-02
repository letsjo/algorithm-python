# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

sumArr = [0]
x = 0
for i in range(N):
    x += arr[i]
    sumArr.append(x)

for _ in range(M):
    i, j = map(int, input().split())
    print(sumArr[j]-sumArr[i-1])
