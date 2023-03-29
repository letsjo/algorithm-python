# 오븐 시계

hour, min = map(int, input().split())
timer = int(input())

min += timer

hour += min // 60
min %= 60
hour %= 24

print(hour, min)
