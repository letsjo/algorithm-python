# 하노이 탑

def move(n, start, target):
    if n > 1:
        move(n-1, start, 6-start-target)

    print(start, target)

    if n > 1:
        move(n-1, 6-start-target, target)


N = int(input())

print(2**N-1)

if (N <= 20):
    move(N, 1, 3)
