# 신입 사원
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    tests = []
    count = 1

    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        tests.append((a, b))

    tests.sort(key=lambda x: x[0])
    cutLineRank = tests[0]
    for scores in tests:
        if cutLineRank[1] > scores[1]:
            cutLineRank = scores
            count += 1

    print(count)
