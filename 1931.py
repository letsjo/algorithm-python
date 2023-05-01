# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())

meeting = []
count = 0

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: (x[1], x[0]))
nextTime = 0

for (start, end) in meeting:
    if start >= nextTime:
        nextTime = end
        count += 1

# while meeting:
#     hour, start, end = heapq.heappop(meeting)
#     isPossible = True
#     for i in range(start, end):
#         if hours[i] == 1:
#             isPossible = False
#             break
#     if isPossible:
#         count += 1
#         for i in range(start, end):
#             hours[i] = 1

print(count)
