# 진법 변환 2

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            mod = chr(55+mod)
        rev_base += str(mod)

    return rev_base[::-1]


N, B = map(int, input().split())

print(solution(N, B))
