# 공유기 설치

N, C = map(int, input().split())
buildings = sorted([int(input()) for _ in range(N)])

start, end = buildings[0], buildings[len(buildings)-1]

minimumDistances = []

while start <= end:
    countRouter = 1
    lastInstalled = 0
    mid = (start + end) // 2
    for index in range(1, len(buildings)):
        distance = buildings[index] - buildings[lastInstalled]
        if (distance >= mid):
            countRouter += 1
            lastInstalled = index
            if (countRouter >= C):
                minimumDistances.append(mid)
                start = mid+1
                break
        if index == len(buildings)-1:
            end = mid-1
            break

print(max(minimumDistances))
