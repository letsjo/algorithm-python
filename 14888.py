# 연산자 끼워넣기

N = int(input())
numbers = list(map(int, input().split()))[:N]
operator = list(map(int, input().split()))[:4]

maximum = -1e9  # inf
minimum = 1e9   # -inf


def dfs(count, total, plus, minus, multi, divide):
    global maximum, minimum
    if count == N-1:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(count+1, total + numbers[count+1], plus-1, minus, multi, divide)
    if minus:
        dfs(count+1, total - numbers[count+1], plus, minus-1, multi, divide)
    if multi:
        dfs(count+1, total * numbers[count+1], plus, minus, multi-1, divide)
    if divide:
        dfs(count+1, int(total / numbers[count+1]),
            plus, minus, multi, divide-1)


dfs(0, numbers[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)
