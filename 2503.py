# 숫자 야구

n = int(input())
games = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(123, 988):
    number = str(i)
    if '0' in number:
        continue
    if number[0] == number[1] or number[1] == number[2] or number[0] == number[2]:
        continue
    correct = True
    for game in games:
        strike, ball = 0, 0
        for j in range(3):
            if number[j] == str(game[0])[j]:
                strike += 1
            elif number[j] in str(game[0]):
                ball += 1
        if strike != game[1] or ball != game[2]:
            correct = False
            break
    if correct:
        answer += 1

print(answer)