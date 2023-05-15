# 인사성 밝은 곰곰이
import sys
input = sys.stdin.readline

N = int(input())
count_emotion = 0
hi_members = {}

for _ in range(N):
    chat = input().strip()
    if chat == 'ENTER':
        hi_members = {}
        continue
    if chat not in hi_members:
        hi_members[chat] = 1
        count_emotion+=1

print(count_emotion)
        