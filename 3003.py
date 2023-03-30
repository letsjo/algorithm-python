# 킹, 퀸, 룩, 비숍, 나이트, 폰

chess = [1, 1, 2, 2, 2, 8]
index = 0
pieces = list(map(int, input().split()))

for piece in pieces:
    pieces[index] = str(chess[index]-piece)
    index += 1

print(' '.join(pieces))
