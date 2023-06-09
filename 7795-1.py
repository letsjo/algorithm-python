# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))

    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    count = 0
    pointer = 0

    for i in range(N):
        for j in range(pointer,M):
            if n_list[i] > m_list[j]:
                count += M-j
                pointer = j
                break
    
    print(count)
