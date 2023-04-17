# 제로
import sys

K = int(input())
input = sys.stdin.readline
stack = []

for _ in range(K):
    number = int(input())
    if stack and number == 0:
        stack.pop()
    elif number > 0:
        stack.append(number)

print(sum(stack))
