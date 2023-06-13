# N과 M (4)

n, m = map(int,input().split())

answer = []

def dfs(index,count):
    if m == count:
        print(*answer)
        return
    
    for i in range(index,n):
        answer.append(i+1)
        dfs(i,count+1)
        answer.pop()

dfs(0,0)
