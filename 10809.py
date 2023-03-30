# 알파벳 찾기

word = input()
wordCode = [ord(letter) for letter in word]
result = []
for code in range(97, 123):
    try:
        result.append(str(wordCode.index(code)))
    except ValueError:
        result.append('-1')

print(' '.join(result))
