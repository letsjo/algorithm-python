# 붙임성 좋은 총총이
import sys
input = sys.stdin.readline

n = int(input())
dic = {}
dic['ChongChong'] = 1

for _ in range(n):
    name1, name2 = input().split()
    if name1 in dic or name2 in dic:
        dic[name1] = 1
        dic[name2] = 1

print(sum(dic.values()))
