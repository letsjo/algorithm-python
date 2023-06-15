# 안전 영역
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
heightList = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,h):
    if (heightList[x][y] <= h or visited[x][y]):
        return
    
    visited[x][y] = True
    for i in range(4):
        if (0<=x+dx[i]<N and 0<=y+dy[i]<N):
            dfs(x+dx[i],y+dy[i],h)

maxCount = 0

for h in range(101):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and heightList[i][j] > h:
                count+=1
                dfs(i,j,h)
    maxCount = max(maxCount,count)
    if count == 0:
        break

print(maxCount)