# 먹을 것인가 먹힐 것인가

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))

    nList.sort(reverse=True)
    mList.sort(reverse=True)
    count = 0
    pointer = 0

    for i in range(N):
        for j in range(pointer,M):
            if nList[i] > mList[j]:
                pointer=j
                count+=M-j
                break

    print(count)