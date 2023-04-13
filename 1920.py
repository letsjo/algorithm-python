# 수 찾기

N = int(input())
checkList = sorted(list(map(int, input().split())))
M = int(input())
findList = list(map(int, input().split()))

for find in findList:
    isFound = False
    halfIndex = int(len(checkList)/2)
    if find >= checkList[halfIndex]:
        for check in checkList[halfIndex:]:
            if find == check:
                isFound = True
                break
        if (isFound):
            print(1)
        else:
            print(0)
