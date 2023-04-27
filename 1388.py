# 바닥 장식

N, M = map(int, input().split())

floor = []

for _ in range(N):
    floor.append(input())

count = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '0':
            continue
        if floor[i][j] == '-':
            k = j
            while k < M and floor[i][k] == '-':
                floor[i] = floor[i][:k] + '0' + floor[i][k+1:]
                k += 1
            count += 1
        elif floor[i][j] == '|':
            k = i
            while k < N and floor[k][j] == '|':
                floor[k] = floor[k][:j] + '0' + floor[k][j+1:]
                k += 1
            count += 1

print(count)
