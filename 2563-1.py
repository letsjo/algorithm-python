# 색종이 2차

countPaper = int(input())
canvas = [[0]*100 for _ in range(100)]
answer = 0

for _ in range(countPaper):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if canvas[i][j] == 0:
                canvas[i][j] = 1
                answer += 1

print(answer)
