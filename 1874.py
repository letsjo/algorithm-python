# 스택 수열
import sys
input = sys.stdin.readline

n = int(input())

stack = []
numbers = []
answers = []

for _ in range(n):
    numbers.append(int(input()))

index = 0
count = 1

while index < n:
    if not stack or stack[-1] < numbers[index]:
        stack.append(count)
        answers.append('+')
        count += 1
    elif stack and stack[-1] == numbers[index]:
        index += 1
        stack.pop()
        answers.append('-')
    else:
        print('NO')
        break
else:
    for answer in answers:
        print(answer)
