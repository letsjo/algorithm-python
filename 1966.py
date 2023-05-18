# 프린터 큐

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(queue[idx], idx) for idx in range(N)]
    count = 0

    while True:
        if queue[0][0] == max(queue)[0]:
            count += 1
            if queue[0][1] == M:
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    print(count)