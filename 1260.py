# DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

N, M, V = map(int, input().split())

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

graph = [[False] * (N+1) for _ in range(N+1)]
queue = deque()
count = 0

for _ in range(M):
    vertex_a, vertex_b = map(int, input().split())
    graph[vertex_a][vertex_b] = graph[vertex_b][vertex_a] = True


def dfs(vertex):
    dfs_visited[vertex] = True
    print(vertex, end=' ')
    for index in range(1, N+1):
        if graph[vertex][index] and dfs_visited[index] == False:
            dfs(index)
    return


def bfs(vertex):
    if bfs_visited[vertex] == False:
        bfs_visited[vertex] = True
        print(vertex, end=' ')
        for index in range(len(graph[vertex])):
            if graph[vertex][index]:
                queue.append(index)
    if queue:
        nextVertex = queue.popleft()
        bfs(nextVertex)


dfs(V)
print()
bfs(V)
