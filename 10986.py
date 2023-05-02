# 나머지 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
sumList = [0] * (N)
restList = [0] * (N)
C = [0] * M

sumList[0] = A[0]
restList[0] = A[0] % M
count = 0

for i in range(1, N):
    sumList[i] = sumList[i-1] + A[i]
    restList[i] = sumList[i] % M

for i in range(N):
    C[restList[i]] += 1

count += C[0]

for i in range(len(C)):
    count += C[i]*(C[i]-1) // 2

print(count)
