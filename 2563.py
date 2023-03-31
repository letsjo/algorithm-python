# 색종이

canvas = [[0 for _ in range(100)] for _ in range(100)]
paperCount = int(input())
answer = 0

for _ in range(paperCount):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if (canvas[i][j] == 0):
                answer += 1
                canvas[i][j] = 1

print(answer)
