# 탈출
import sys
from collections import deque
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

R, C = map(int, input().split())

forestMap = []
visited = [[False]*C for _ in range(R)]

for _ in range(R):
    forestMap.append(list(input().strip()))

queue = deque()
river = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

escapeCave = [-1, -1]


def sol():
    for i in range(R):
        for j in range(C):
            if forestMap[i][j] == 'S':
                forestMap[i][j] == '.'
                queue.append([i, j, 0])
            if forestMap[i][j] == '*':
                river.append([i, j])

    while queue:
        countRiver = len(river)
        for _ in range(countRiver):
            rx, ry = river.popleft()
            for k in range(4):
                nrx = rx + dx[k]
                nry = ry + dy[k]
                if 0 <= nrx < R and 0 <= nry < C and (forestMap[nrx][nry] == '.'):
                    visited[nrx][nry] = True
                    forestMap[nrx][nry] = '*'
                    river.append([nrx, nry])

        countQueue = len(queue)
        for _ in range(countQueue):
            x, y, moveCount = queue.popleft()
            if (forestMap[x][y] == 'D'):
                return moveCount
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False and (forestMap[nx][ny] == '.' or forestMap[nx][ny] == 'D'):
                    visited[nx][ny] = True
                    queue.append([nx, ny, moveCount+1])

    return 'KAKTUS'


result = sol()

print(result)
