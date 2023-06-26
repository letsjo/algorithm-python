# 팰린드롬 만들기

import sys
input = sys.stdin.readline

dic = {}
s = input().rstrip()

for i in s:
    if dic.get(i):
        dic[i] += 1
    else:
        dic[i] = 1

center = ''
for k,v in dic.items():
    if v % 2 == 1:
        if center != '':
            print("I'm Sorry Hansoo")
            exit(0)
        center = k

answer = ''
for k,v in sorted(dic.items()):
    answer+=k*(v//2)
print(answer+center+answer[::-1])