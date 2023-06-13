# N과 M (3)

n, m = map(int,input().split())

answer = []

def dfs(count):
    if count == m:
        print(*answer)
        return
    for i in range(n):
        answer.append(i+1)
        dfs(count+1)
        answer.pop()

dfs(0)