# 단지번호붙이기

N = int(input())

areaMap = []
visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = [0]

for _ in range(N):
    areaMap.append(list(map(int, input().strip())))


def dfs(x, y, field):
    for direction in range(4):
        nx = dx[direction]+x
        ny = dy[direction]+y
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if areaMap[nx][ny] == 1:
                answer[field] += 1
                dfs(nx, ny, field)


for i in range(N):
    for j in range(N):
        if areaMap[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            answer[0] += 1
            answer.append(1)
            dfs(i, j, answer[0])

print(answer[0])
a = sorted(answer[1:])

for i in range(len(a)):
    print(a[i])
