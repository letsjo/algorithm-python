# 별 찍기 - 10
import sys
sys.setrecursionlimit(10**6)

n = int(input())
star = [[' '] * n for _ in range(n)]

def draw(x,y,n):
    if n == 1:
        star[x][y] = '*'
        return
    n //= 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw(x+(n*i), y+(n*j), n)

draw(0,0,n)

for i in range(n):
    for j in range(n):
        print(star[i][j],end='')
    print()