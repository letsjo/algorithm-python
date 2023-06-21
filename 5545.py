# 최고의 피자

import sys
input = sys.stdin.readline

n = int(input())
dough_price, topic_price = map(int,input().split())
dough = int(input())
topic = [0]*n
for i in range(n):
    topic[i] = int(input())

topic.sort(reverse=True)

answer = dough / dough_price
total_cal = dough
total_price = dough_price

for i in range(n):
    tmp = (total_cal + topic[i]) / (total_price+topic_price)
    if tmp > answer:
        answer = tmp
        total_cal += topic[i]
        total_price += topic_price

print(int(answer))