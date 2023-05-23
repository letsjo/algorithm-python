# 통계학
import sys
input = sys.stdin.readline

N = int(input())
dic = {}
arr = []
sum = 0

for _ in range(N):
    n = int(input().strip())
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    arr.append(n)
    sum += n

dic_list = sorted(dic.items(),key = lambda x:(-x[1],x[0]))
arr.sort()
print(round(sum/N))
print(arr[N//2])
if N>1 and dic_list[0][1] == dic_list[1][1]:
    print(dic_list[1][0])
else:
    print(dic_list[0][0])
print(arr[N-1]-arr[0])