# 분수찾기
# 1 3 6 10
#  2+3+4

X = int(input())
until = 1
count = 2
lineCount = 0
while True:
    lineCount += 1
    if X <= until:
        break
    until += count
    count += 1

if (lineCount % 2 == 0):
    print(f'{lineCount-(until-X)}/{until-X+1}')
else:
    print(f'{until-X+1}/{lineCount-(until-X)}')
