# 팩토리얼

def solution(n):
    if (n == 0 | n == 1):
        return 1

    return n*solution(n-1)


print(solution(int(input())))
