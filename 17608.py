# 막대기
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    number = int(input())
    if not stack:
        stack.append(number)
        continue
    while stack and number >= stack[-1]:
        stack.pop()
    stack.append(number)
print(len(stack))
