# 참외밭

k = int(input())
arr = [list(map(int,input().split())) for _ in range(6)]

max_w = 0
max_h = 0
index_max_w = 0
index_max_h = 0

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_w < arr[i][1]:
            max_w = arr[i][1]
            index_max_w = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if max_h < arr[i][1]:
            max_h = arr[i][1]
            index_max_h = i

empty_w = abs(arr[(index_max_w - 1) % 6][1] - arr[(index_max_w + 1) % 6][1])
empty_h = abs(arr[(index_max_h - 1) % 6][1] - arr[(index_max_h + 1) % 6][1])

answer = ((max_w*max_h) - (empty_w*empty_h)) * k
print(answer)