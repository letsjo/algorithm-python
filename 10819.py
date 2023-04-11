# 차이를 최대로

n = int(input())
in_list = list(map(int, input().split()))
visited = [False]*n
answer = 0


def solution(li):
    global answer
    if len(li) == n:
        total = 0
        for i in range(n-1):
            total += abs(li[i] - li[i+1])
        answer = max(answer, total)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            li.append(in_list[i])
            solution(li)
            visited[i] = False
            li.pop()


solution([])
print(answer)

# 순열 사용해보기

# import itertools

# n = int(input())
# in_list = list(map(int, input().split()))

# permutationList = itertools.permutations(in_list, n)

# answer = 0
# for mixedList in permutationList:
#     total = 0
#     for i in range(n-1):
#         total += abs(mixedList[i]-mixedList[i+1])
#     answer = max(answer, total)

# print(answer)
