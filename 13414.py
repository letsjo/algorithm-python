# 수강신청
import sys
input = sys.stdin.readline

k, l = map(int, input().split())

dic_count = {}
answer = []

for i in range(l):
    number = input()
    dic_count[number] = i

answer = sorted(dic_count.items(), key=lambda x:(x[1]))

min = k

if k > len(answer):
    min = len(answer) 

for i in range(min):
    print(answer[i][0])

