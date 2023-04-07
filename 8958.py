# OX퀴즈

T = int(input())

for _ in range(T):
    answer = 0
    i = 1
    for result in input():
        if 'O' in result:
            answer += i
            i += 1
        else:
            i = 1
    print(answer)
