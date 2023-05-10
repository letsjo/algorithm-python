# 1로 만들기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
visited = [0]*(N+1)
queue.append(N)

while queue:
    number = queue.popleft()
    if number == 1:
        break

    if number % 3 == 0 and visited[int(number//3)] == 0:
        queue.append(int(number//3))
        visited[int(number//3)] += visited[number] + 1

    if number % 2 == 0 and visited[int(number//2)] == 0:
        queue.append(int(number//2))
        visited[int(number//2)] += visited[number] + 1

    if visited[number-1] == 0:
        queue.append(number-1)
        visited[number-1] += visited[number]+1

print(visited[1])

# dfs 는 최소를 구하는데 적합하지 않음
# solution(10) -> 4

# def solution(N):
#     global answer
#     if N == 1:
#         return answer

#     if N % 3 == 0:
#         answer += 1
#         return solution(N/3)

#     if N % 2 == 0:
#         answer += 1
#         return solution(N/2)

#     answer += 1
#     return solution(N-1)
