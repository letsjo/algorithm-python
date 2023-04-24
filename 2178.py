# 미로 탐색
from collections import deque

N, M = map(int, input().split())
mazeMap = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    mazeMap.append(list(input()))

queue = deque()
mazeMap[0][0] = 1
queue.append([0, 0])
count = 1

while True:
    x, y = queue.popleft()
    if x == N-1 and y == M-1:
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M:
            if mazeMap[nx][ny] == '1':
                queue.append([nx, ny])
                mazeMap[nx][ny] = mazeMap[x][y] + 1

print(mazeMap[N-1][M-1])
