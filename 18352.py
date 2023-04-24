# 특정 거리의 도시 찾기
from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
city = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

queue = deque()
queue.append(X)

distance[X] = 0

while queue:
    now = queue.popleft()
    for nextCity in graph[now]:
        if distance[nextCity] == -1:
            distance[nextCity] = distance[now] + 1
            queue.append(nextCity)

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        city = True

if not city:
    print(-1)
