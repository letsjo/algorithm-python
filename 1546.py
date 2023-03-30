# 평균

M = int(input())
scores = list(map(int, input().split(' ')))
bestScore = max(scores)
totalFakeScore = 0

for score in scores:
    totalFakeScore += score/bestScore*100

print(totalFakeScore/M)
