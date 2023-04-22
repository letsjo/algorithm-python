# 이분 그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())
answer = True


def dfs(vertex, color):
    global answer
    vertex_color[vertex] = color

    for i in graph[vertex]:
        if vertex_color[i] == color:
            answer = False
            return

        if vertex_color[i] == 0:
            dfs(i, -1 * color)


for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        vertex_a, vertex_b = map(int, input().split())
        graph[vertex_a].append(vertex_b)
        graph[vertex_b].append(vertex_a)

    vertex_color = [0] * (V+1)
    answer = True

    for i in range(1, V+1):
        if not answer:
            break

        if vertex_color[i] == 0:
            dfs(i, 1)

    print('YES' if answer else 'NO')
