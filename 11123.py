# 양 한마리... 양 두마리...
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
    h,w = map(int,input().split())
    visited = [[False] * w for _ in range(h)]
    maps = [list(input()) for _ in range(h)]
    answer = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def dfs(x,y):
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and maps[nx][ny] == '#':
                dfs(nx,ny)
        
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '#' and not visited[i][j]:
                answer += 1
                dfs(i,j)
    
    print(answer)