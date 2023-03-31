# 최댓값

maxNumber = 0
position = ['1', '1']

for i in range(9):
    lines = list(map(int, input().split()))

    for j in range(9):
        if maxNumber < lines[j]:
            maxNumber = lines[j]
            position[0] = str(i+1)
            position[1] = str(j+1)

print(maxNumber)
print(' '.join(position))
