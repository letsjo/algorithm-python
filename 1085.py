# 직사각형에서 탈출

result = list(map(int, input().split()))

result[2] -= result[0]
result[3] -= result[1]

print(min(result))
