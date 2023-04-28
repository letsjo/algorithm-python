# LCS 3

stringA = input()
stringB = input()
stringC = input()

lengthA = len(stringA)
lengthB = len(stringB)
lengthC = len(stringC)

dp = [[[0] * (lengthC+1) for _ in range(lengthB+1)] for _ in range(lengthA+1)]

for i in range(1, lengthA+1):
    for j in range(1, lengthB+1):
        for k in range(1, lengthC+1):
            if stringA[i-1] == stringB[j-1] and stringB[j-1] == stringC[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[lengthA][lengthB][lengthC])
