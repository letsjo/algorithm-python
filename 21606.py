# 아침 산책

# 새로운 알고리즘 200점

# 실외에서 갈 수 있는 경우의 수 n 을 알아내서
# n * (n-1) 으로 경우의 수만 계산하는 방법

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = input().rstrip()
indoor = [0] * (N+1)
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
answer = 0

for i in range(len(A)):
    if A[i] == '1':
        indoor[i+1] = 1

for _ in range(N-1):
    vertex_a, vertex_b = map(int, input().split())
    graph[vertex_a].append(vertex_b)
    graph[vertex_b].append(vertex_a)


def dfs(vertex):
    res = 0

    for i in graph[vertex]:
        if indoor[i] == 0:
            if not visited[i]:
                visited[i] = 1
                res += dfs(i)
        else:
            res += 1
    return res


for i in range(1, N+1):
    if indoor[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            answer += res * (res-1)
    else:
        for next_node in graph[i]:
            if indoor[next_node] == 1:
                answer += 1


print(answer)

# 60점 코드

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# A = input().rstrip()
# indoor = [0] * (N+1)
# visited = [[False] * (N+1) for _ in range(N+1)]
# graph = [[] for _ in range(N+1)]
# answer = 0

# for i in range(len(A)):
#     if A[i] == '1':
#         indoor[i+1] = 1

# for _ in range(N-1):
#     vertex_a, vertex_b = map(int, input().split())
#     graph[vertex_a].append(vertex_b)
#     graph[vertex_b].append(vertex_a)

# def dfs(start, vertex):
#     global answer
#     visited[start][vertex] = True

#     for i in graph[vertex]:
#         if not visited[start][i]:
#             if indoor[i] == 0:
#                 dfs(start, i)
#             else:
#                 answer += 1
#     return

# for i in range(1, N+1):
#     if indoor[i] == 1:
#         dfs(i, i)

# print(answer)
