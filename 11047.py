# 동전 0
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
coins = deque()

for _ in range(N):
    coins.append(int(input()))

answer = 0

while K > 0:
    coin = coins.pop()
    answer += K // coin
    K %= coin

print(answer)
