# 벽 부수고 이동하기
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

game_map = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited_break = [[False]*m for _ in range(n)]

count = 0

queue = deque()
queue.append((0,0,0,0))
visited[0][0] = True
visited_break[0][0] = True

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = -1

while queue:
    x, y, count, break_count = queue.popleft()

    if x == m-1 and y == n-1:
        answer = count+1
        break

    for i in range(4):
        nextX = x+dx[i]
        nextY = y+dy[i]
        if (0<=nextX<m and 0<=nextY<n):
            if game_map[nextY][nextX] == '1' and break_count == 0 and not visited_break[nextY][nextX]:
                visited_break[nextY][nextX] = True
                queue.append((nextX,nextY,count+1,break_count+1))
            elif game_map[nextY][nextX] == '0' and break_count == 1 and not visited_break[nextY][nextX]:
                visited_break[nextY][nextX] = True
                queue.append((nextX,nextY,count+1,break_count))
            elif game_map[nextY][nextX] == '0' and break_count == 0 and not visited[nextY][nextX]:
                visited[nextY][nextX] = True
                queue.append((nextX,nextY,count+1,break_count))

print(answer)