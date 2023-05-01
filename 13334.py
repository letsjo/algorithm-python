# 철로
import sys
import heapq
input = sys.stdin.readline

location = []

for _ in range(int(input())):
    info = list(map(int, input().split()))
    if info[0] > info[1]:
        info[0], info[1] = info[1], info[0]
    location.append(info)

location.sort(key=lambda x: x[1])
distance = int(input())
heap = []
maxPath = 0

for info in location:
    startPoint = info[1] - distance
    if info[0] >= startPoint:
        heapq.heappush(heap, info)
    while heap and heap[0][0] < startPoint:
        heapq.heappop(heap)

    maxPath = max(maxPath, len(heap))

print(maxPath)
