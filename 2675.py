# 문자열 반복

T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    for letter in S:
        print(letter*int(R), end='')
    print()
