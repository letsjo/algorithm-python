# 토마토
import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

boxes = []

for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    boxes.append(box)

visited = [[[False]*M for _ in range(N)] for _ in range(H)]

queue = deque()
state = True
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def checkBoxes():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 1:
                    queue.append([i, j, k, 0])

    while queue and state:
        x, y, z, day = queue.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and visited[nx][ny][nz] == False:
                visited[nx][ny][nz] = True
                if boxes[nx][ny][nz] == 0:
                    boxes[nx][ny][nz] = 1
                    queue.append([nx, ny, nz, day+1])

    for i in range(H):
        for j in range(N):
            for k in range(M):
                visited[i][j][k] = False
                if boxes[i][j][k] == 0:
                    return -1

    return day


result = checkBoxes()

print(result)
