# 연결 요소의 개수

import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


def dfs(vertex):
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            dfs(i)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        print('dfs', i)
        dfs(i)
        count += 1

print(count)
