# N과 M (7)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []

def dfs(count):
    if count == m:
        print(*answer)
        return
    
    for i in range(n):
        answer.append(arr[i])
        dfs(count+1)
        answer.pop()

dfs(0)