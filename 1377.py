# 버블 소트
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()),i))

arr.sort()

ans = 0
for i in range(n):
    ans = max(ans, arr[i][1]-i)

print(ans+1)