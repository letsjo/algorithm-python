# 01타일
import sys

input = sys.stdin.readline

n = int(input())
prev_prev = 2
prev = 3

if n <= 3:
    print(n)
else:
    for i in range(4, n+1):
        curr = prev_prev + prev
        prev_prev = prev
        prev = curr % 15746

    print(prev)
