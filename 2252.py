# 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

inDegree = [0]*(N+1)
answer = [None]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    inDegree[b] += 1
    graph[a].append(b)

queue = deque()

for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

for i in range(1, N+1):
    x = queue.popleft()
    answer[i] = x
    for j in range(len(graph[x])):
        y = graph[x][j]
        inDegree[y] -= 1
        if (inDegree[y] == 0):
            queue.append(y)

for i in range(1, N+1):
    print(answer[i], end=' ')
