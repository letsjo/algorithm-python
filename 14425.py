# 문자열 집합

N, M = map(int,input().split())

dic = {}
count = 0

for _ in range(N):
    dic[input().strip()]=1

for _ in range(M):
    if input() in dic:
        count+=1

print(count)