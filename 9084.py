# 동전

T = int(input())


def solution(coins, value):
    dp = [0]*(value+1)
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], value+1):
            dp[j] += dp[j - coins[i]]
    return dp[value]


for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    value = int(input())
    count = solution(coins, value)
    print(count)
