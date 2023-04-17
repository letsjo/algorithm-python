# 괄호의 값

import sys

input = sys.stdin.readline
string = input()
stack = []
calculator = 1
answer = 0

for index in range(len(string)):
    if string[index] == '(':
        stack.append(string[index])
        calculator *= 2
    elif string[index] == '[':
        stack.append(string[index])
        calculator *= 3
    elif string[index] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if string[index-1] == '(':
            answer += calculator
        stack.pop()
        calculator //= 2

    elif string[index] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if string[index-1] == '[':
            answer += calculator
        stack.pop()
        calculator //= 3

if stack:
    print(0)
else:
    print(answer)
