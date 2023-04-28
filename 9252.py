# LCS 2

stringA = input()
stringB = input()

lengthA = len(stringA)
lengthB = len(stringB)


count = 0
dp = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]

for i in range(1, lengthA+1):
    for j in range(1, lengthB+1):
        if stringA[i-1] == stringB[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[lengthA][lengthB])

i = lengthA
j = lengthB
lcs = ''

while i > 0 and j > 0:
    if stringA[i - 1] == stringB[j - 1]:
        lcs = stringA[i - 1] + lcs
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(lcs)
