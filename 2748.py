# 피보나치 수 2
import sys

input = sys.stdin.readline

N = int(input())
prev_prev = 1
prev = 2

if N == 0:
    print(0)
elif N == 1:
    print(1)
elif N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    for i in range(4, N+1):
        curr = prev_prev + prev
        prev_prev = prev
        prev = curr

    print(prev)
