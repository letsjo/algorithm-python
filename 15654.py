# N과 M (5)

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False for _ in range(n)]
answer = []

def dfs(count):
    if count == m:
        print(*answer)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            dfs(count+1)
            visited[i] = False
            answer.pop()

dfs(0)