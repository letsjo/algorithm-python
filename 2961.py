# 도영이가 만든 맛있는 음식

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min = 1000000000
for i in range(1, n + 1):
    for j in combinations(s, i):
        sour = 1
        bitter = 0
        for k in j:
            sour *= k[0]
            bitter += k[1]
        if abs(sour - bitter) < min:
            min = abs(sour - bitter)

print(min)

