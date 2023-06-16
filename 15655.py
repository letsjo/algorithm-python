# N과 M (6)

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False for _ in range(n)]
answer = []

def dfs(index,count):
    if count == m:
        print(*answer)
        return
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            dfs(i,count+1)
            answer.pop()
            visited[i] = False

dfs(0,0)