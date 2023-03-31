# 그룹 단어 체커

N = int(input())
answer = N

for _ in range(N):
    letters = []
    word = input()
    wordWithSpace = word + ' '
    index = 1
    for letter in word:
        if letter != wordWithSpace[index]:
            if letter in letters:
                answer -= 1
                break
            letters.append(letter)
        index += 1

print(answer)
