# N과 M (2)

n, m = map(int,input().split())

visited = [False] * n
answer = []

def dfs(index,count):
    if count == m:
        print(*answer)
        return
    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            answer.append(i+1)
            dfs(i,count+1)
            visited[i] = False
            answer.pop()

dfs(0,0)