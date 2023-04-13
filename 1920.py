# 수 찾기

N = int(input())
sortedArr = sorted(list(map(int, input().split())))
M = int(input())
findList = list(map(int, input().split()))


def binarySearch(start, end, target):
    if (start > end):
        return -1
    mid = (start+end)//2

    if (sortedArr[mid] == target):
        return mid
    if (sortedArr[mid] > target):
        return binarySearch(start, mid-1, target)
    return binarySearch(mid+1, end, target)


for find in findList:
    index = binarySearch(0, len(sortedArr)-1, find)
    print('1' if index >= 0 else '0')
