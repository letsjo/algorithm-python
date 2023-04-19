# 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

N = int(input())
maxHeap = []
minHeap = []

for _ in range(N):
    number = int(input())
    if (len(maxHeap) == len(minHeap)):
        heapq.heappush(maxHeap, (-number, number))
    else:
        heapq.heappush(minHeap, number)

    if minHeap and maxHeap[0][1] >= minHeap[0]:
        heapq.heappush(minHeap, heapq.heappop(maxHeap)[1])
        tmp = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, (-tmp, tmp))
    print(maxHeap[0][1])
