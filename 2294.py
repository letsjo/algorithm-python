# 동전 2
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

n, k = map(int, input().split())
coins = []
visited = [False]*(k+1)

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)


def minimumCoin(coins, limit):
    collect = deque()
    for coin in coins:
        collect.append([1, coin])
    while collect:
        count, total = collect.popleft()
        if total == limit:
            return count

        for coin in coins:
            if (total + coin <= limit) and visited[total + coin] == False:
                visited[total+coin] = True
                collect.append([count+1, total + coin])
    return -1


print(minimumCoin(coins, k))
