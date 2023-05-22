# 영단어 암기는 괴로워
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

word = {}
answer = []

for i in range(N):
    w = input().strip()
    if len(w) >= M:
        if w in word:
            word[w] += 1
        else:
            word[w] = 1

answer = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(answer)):
    print(answer[i][0])
    