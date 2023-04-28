# 평범한 배낭

N, K = map(int, input().split())  # 물품수 , 배낭무게

weight = [0]*(N+1)
value = [0]*(N+1)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    weight[i+1], value[i+1] = map(int, input().split())

dp[0][0] = 0

for i in range(N+1):
    for j in range(K+1):
        if j < weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

print(dp[N][K])
