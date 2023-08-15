# 동전 1
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
coins = []

for i in range(a):
    coins.append(int(input()))

dp = [0]*(b+1)

dp[0] = 1

for i in range(a):
    for j in range(coins[i], b+1):
        dp[j] += dp[j-coins[i]]

print(dp[b])
