# Buy One Get One Free

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
high = []
low = []

for _ in range(n):
    quality = int(input())
    high.append(quality)

for _ in range(m):
    quality = int(input())
    low.append(quality)

high.sort(reverse=True)
low.sort(reverse=True)

high_idx = 0
low_idx = 0

answer = 0

while True:
    if low_idx >= m or high_idx >= n:
        break
    if high[high_idx] > low[low_idx]:
        high_idx += 1
        low_idx += 1
        answer += 2
    else:
        low_idx += 1


answer += n - high_idx
print(answer)


