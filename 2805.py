# 나무 자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)

while start <= end:
    getWood = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            getWood += tree - mid
    if getWood >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
