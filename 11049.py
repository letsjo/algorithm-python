# 행렬 곱셈 순서

N = int(input())

R = [0]*N
C = [0]*N

for n in range(N):
    r, c = map(int, input().split())
    R[n] = r
    C[n] = c


# def solution(X, Y):
#     if Y-X <= 0:
#         return 0
#     minimum = 1e9
#     for k in range(X, Y):
#         minimum = min(minimum, solution(X, k)+solution(k+1, Y)+R[X]*C[k]*C[Y])
#     return minimum

# dp 추가
dp = [[0]*N for _ in range(N)]


def solution(X, Y):
    if dp[X][Y] > 0:
        return dp[X][Y]
    if Y-X <= 0:
        return 0
    dp[X][Y] = float('inf')
    for k in range(X, Y):
        dp[X][Y] = min(dp[X][Y], solution(X, k) +
                       solution(k+1, Y)+R[X]*C[k]*C[Y])
    return dp[X][Y]


print(solution(0, N-1))
