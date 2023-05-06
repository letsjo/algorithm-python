# 오큰수
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
answer = [-1]*N
remember_index = 0

for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        answer[stack.pop()] = A[i]

    stack.append(i)

print(*answer)
