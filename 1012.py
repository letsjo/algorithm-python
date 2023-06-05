# 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        for i in range(4):
            dfs(x + mx[i], y + my[i])
        return True
    return False

for _ in range(t):
    n, m, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]

    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1
    
    print(count)




