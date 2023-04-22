# 트리의 부모 찾기
import sys
sys.setrecursionlimit(100010)

N = int(input())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
parent = [0]*(N+1)

while True:
    try:
        vertex_a, vertex_b = map(int, input().split())
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)
    except:
        break

for index in range(len(graph)):
    graph[index].sort()  # [[], [4, 6], [4], [5, 6], [1, 2, 7], [3], [1, 3], [4]]


def dfs(vertex):
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            parent[i] = str(vertex)
            dfs(i)


dfs(1)
print(*parent[2:], sep='\n')
