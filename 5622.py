# 다이얼

dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
answer = 0
for letter in word:
    number = 0
    for dial in dials:
        if letter in dial:
            answer += number+3
            break
        number += 1

print(answer)
