# 탑
import sys
input = sys.stdin.readline

N = int(input())
stack = []
index_stack = []
result = ['0']
index = 0
remember_index = 0


for tower in list(map(int, input().split())):
    index += 1
    if not stack:
        index_stack.append(index)
        stack.append(tower)
        continue
    while stack and tower >= stack[-1]:
        index_stack.pop()
        stack.pop()
    result.append(str(index_stack[-1]) if index_stack else '0')
    index_stack.append(index)
    stack.append(tower)

print(' '.join(result))
