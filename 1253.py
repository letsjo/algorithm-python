# 좋다

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for target in range(N):
    start = 0
    end = N-1
    while start < end:
        if start >= end:
            break

        if target == start:
            start += 1
            continue
        elif target == end:
            end -= 1
            continue

        result = arr[start] + arr[end]

        if result == arr[target]:
            count += 1
            break
        elif result > arr[target]:
            end -= 1
        else:
            start += 1

print(count)
