# 수 찾기

N = int(input())
checkList = sorted(list(map(int, input().split())))
M = int(input())
findList = list(map(int, input().split()))

for find in findList:
    if find in checkList:
        print('1')
    else:
        print('0')
