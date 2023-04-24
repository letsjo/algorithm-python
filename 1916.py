# 최소비용 구하기

# from collections import deque

# N = int(input())
# M = int(input())

# busMap = [[-1]*(N+1) for _ in range(N+1)]
# station = [1e9] * (N+1)

# for _ in range(M):
#     a, b, weight = map(int, input().split())
#     busMap[a][b] = weight

# start, end = map(int, input().split())
# queue = deque()
# station[start] = 0
# queue.append(start)

# while queue:
#     vertex = queue.popleft()
#     if vertex == end:
#         continue
#     for i in range(len(busMap[vertex])):
#         if busMap[vertex][i] != -1:
#             queue.append(i)
#             station[i] = min(station[vertex]+busMap[vertex][i], station[i])

# print(station[end])

# ====
# pypy3 : 메모리 초과
# python3 : 시간 초과
#
# 인접 행렬 -> 인접 리스트 변경
# 큐 -> 우선순위 큐 & heap 변경

import heapq

N = int(input())
M = int(input())

busList = [[] for _ in range(N+1)]
station = [1e9] * (N+1)

for _ in range(M):
    a, b, weight = map(int, input().split())
    busList[a].append([weight, b])

start, end = map(int, input().split())

station[start] = 0
queue = [(station[start], start)]

while queue:
    weight, now = heapq.heappop(queue)
    if station[now] < weight:
        continue
    for nextStation in busList[now]:
        cost = weight + nextStation[0]
        if station[nextStation[1]] > cost:
            station[nextStation[1]] = cost
            heapq.heappush(queue, (cost, nextStation[1]))

print(station[end])
