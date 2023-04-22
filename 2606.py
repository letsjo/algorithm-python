# 바이러스

import sys
sys.setrecursionlimit(10000)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

count = 0


def dfs(vertex):
    global count
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            count += 1
            dfs(i)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, n+1):
    if not visited[i]:
        dfs(1)

print(count)
