# 괄호

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    parenthesisString = input()
    stack = []
    for index in range(len(parenthesisString)):
        if parenthesisString[index] == '(':
            stack.append('0')
        elif parenthesisString[index] == ')' and stack:
            stack.pop()
        elif parenthesisString[index] == ')' and not stack:
            stack.append('0')
            break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
