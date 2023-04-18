# 최대 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    number = int(input())
    if numbers and number == 0:
        print(heapq.heappop(numbers)[1])
    elif not numbers and number == 0:
        print(0)
    else:
        heapq.heappush(numbers, (-number, number))
