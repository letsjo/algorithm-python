# 벌집

# 1 7 19 37 61
# 6 12 18 24

number = int(input())
cycle = 0
until = 1
answer = 0

while True:
    cycle += 1
    if number <= until:
        answer = cycle
        break
    until += cycle*6

print(answer)
