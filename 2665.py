# 미로 만들기
import sys
import heapq

input = sys.stdin.readline

n = int(input())
mazeMap = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    mazeMap.append(list(map(int, input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited[0][0] = 0
queue = []
heapq.heappush(queue, (0, 0, 0))

while queue:
    count, x, y = heapq.heappop(queue)
    if x == n-1 and y == n-1:
        print(count)
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if mazeMap[nx][ny] == 0:
                heapq.heappush(queue, (count + 1, nx, ny))
            else:
                heapq.heappush(queue, (count, nx, ny))
