# 경쟁적 전염

import sys
from collections import deque
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

N, K = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virusMap = []
visited = [[False]*N for _ in range(N)]

queue = deque()

for _ in range(N):
    virusMap.append(list(map(int, input().split())))

second = 0

S, X, Y = map(int, input().split())

for number in range(1, K+1):
    for i in range(N):
        for j in range(N):
            if virusMap[i][j] == number:
                queue.append([i, j, number])

while queue:
    countQueue = len(queue)
    if second >= S:
        break
    second += 1
    for _ in range(countQueue):
        x, y, number = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                visited[nx][ny] = True
                if virusMap[nx][ny] == 0:
                    virusMap[nx][ny] = number
                    queue.append([nx, ny, number])

print(virusMap[X-1][Y-1])
