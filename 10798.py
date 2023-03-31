# 세로읽기

lines = []
maxLength = 0
result = ''
for i in range(5):
    word = input()
    wordLength = len(word)
    if (maxLength < wordLength):
        maxLength = wordLength
    lines.append(word)

for j in range(maxLength):
    for i in range(5):
        try:
            result += lines[i][j]
        except:
            result += ''

print(result)
