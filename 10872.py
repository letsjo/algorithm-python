# 팩토리얼

N = int(input())

if (N == 0 | N == 1):
    print(1)

else:
    answer = 1
    for i in range(2, N+1):
        answer *= i

    print(answer)
