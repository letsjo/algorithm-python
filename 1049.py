# 기타줄

n, m = map(int, input().split())

single = 1e9
bundle = 1e9

for _ in range(m):
    a, b = map(int, input().split())
    bundle = min(a, bundle)
    single = min(b, single)

answer = 0

all_single = n * single

while n > 0:
    if single * n < bundle:
        answer += single * n
        n -= n
    else:
        answer += bundle
        n -= 6

print(min(answer,all_single))

