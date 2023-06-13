# N과 M (1)

n, m = map(int,input().split())

visited = [False] * n
answer = []

def dfs(count):
    if count == m:
        print(*answer)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(i+1)
            dfs(count+1)
            visited[i] = False
            answer.pop()

dfs(0)