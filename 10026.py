# 적록색약
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n = int(input())
painting = [input() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
rg_visited = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
rg_count = 0

def dfs(x,y,target):
    if (painting[x][y] != target or visited[x][y]):
        return
    
    visited[x][y] = True
    for i in range(4):
        if (0<=x+dx[i]<n and 0<=y+dy[i]<n):
            dfs(x+dx[i],y+dy[i],target)

def rg_dfs(x,y,target):
    if target == 'B':
        if (painting[x][y] != 'B' or rg_visited[x][y]):
            return
    else:
        if (painting[x][y] == 'B' or rg_visited[x][y]):
            return
    
    rg_visited[x][y] = True
    for i in range(4):
        if (0<=x+dx[i]<n and 0<=y+dy[i]<n):
            rg_dfs(x+dx[i],y+dy[i],target)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count+=1
            dfs(i,j,painting[i][j])
        if not rg_visited[i][j]:
            rg_count+=1
            rg_dfs(i,j,painting[i][j])

print(count,rg_count)