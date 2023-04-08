# 종이자르기

[width, height] = list(map(int, input().split()))
paper = [height, width]
cutting = [[], []]

for countCut in range(int(input())):
    [direction, point] = list(map(int, input().split()))
    cutting[direction].append(point)

cutting[0].sort(reverse=True)
cutting[1].sort(reverse=True)

cutting[0].append(0)
cutting[1].append(0)

print(cutting)

max = [0, 0]
for i in range(2):
    for point in cutting[i]:
        gap = paper[i] - point
        paper[i] = point
        if (max[i] <= gap):
            max[i] = gap
    if max[i] == 0:
        max[i] = paper[i]

print(max[0]*max[1])
